# -*- coding: UTF-8 -*-

'''
Module
    subprocessor_test.py
Copyright
    Copyright (C) 2021 - 2026 Vladimir Roncevic <elektron.ronca@gmail.com>
    gen_dbus is free software: you can redistribute it and/or modify it
    under the terms of the GNU General Public License as published by the
    Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.
    gen_dbus is distributed in the hope that it will be useful, but
    WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
    See the GNU General Public License for more details.
    You should have received a copy of the GNU General Public License along
    with this program. If not, see <http://www.gnu.org/licenses/>.
Info
    Defines unit tests for SubProcessor adapter.
'''

from __future__ import annotations

from collections.abc import Mapping
from os import makedirs
from os.path import exists, join
from tempfile import TemporaryDirectory
from unittest import TestCase, main
from unittest.mock import Mock

from ats_utilities.exceptions import ATSTypeError, ATSValueError
from ats_utilities.generation.imanager import IGeneratorManager
from ats_utilities.logger.ilogger import ILogger

from gen_dbus.core.model.bus_type import BusType
from gen_dbus.core.model.dbus_role import DBusRole
from gen_dbus.core.model.project_setup import ProjectSetup
from gen_dbus.core.model.project_type import ProjectType
from gen_dbus.infrastructure.ischeme_builder import ISchemeBuilder
from gen_dbus.infrastructure.scheme_builder import SchemeBuilder
from gen_dbus.infrastructure.subprocessor import SubProcessor
from gen_dbus.setup.bundle import GenDBusBundle
from gen_dbus.setup.factory import GenDBusBundleFactory

__author__ = 'Vladimir Roncevic'
__copyright__ = 'Copyright (C) 2021 - 2026 Vladimir Roncevic <elektron.ronca@gmail.com>'
__credits__ = ['Vladimir Roncevic', 'Python Software Foundation']
__license__ = 'https://github.com/vroncevic/gen_dbus/blob/dev/LICENSE'
__version__ = '1.1.6'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Updated'


class TestSubProcessor(TestCase):
    '''
        Defines unit tests for SubProcessor adapter.

        It defines:

            :methods:
                | test_init_validation - Verifies constructor validates collaborators.
                | test_run_success_and_nested_logging - Verifies template generation and file logging.
                | test_run_real_templates - Verifies end-to-end generation across types and roles.
                | test_run_failures - Verifies unsuccessful generation and invalid setup errors.
                | test_state_and_str - Verifies is_initialized and string representation.
    '''

    def test_init_validation(self) -> None:
        '''
            Verifies constructor validates collaborators.

            :exceptions: None.
        '''
        invalid_none: object = None
        invalid_type: object = 'invalid'
        valid_generator: Mock = Mock(spec=IGeneratorManager)
        valid_generator.get_context.return_value = Mock(logger=Mock(spec=ILogger))
        valid_builder: SchemeBuilder = SchemeBuilder()

        with self.assertRaises(ATSValueError):
            SubProcessor(generator=invalid_none, scheme_builder=valid_builder)  # type: ignore[arg-type]

        with self.assertRaises(ATSTypeError):
            SubProcessor(generator=invalid_type, scheme_builder=valid_builder)  # type: ignore[arg-type]

        with self.assertRaises(ATSValueError):
            SubProcessor(generator=valid_generator, scheme_builder=invalid_none)  # type: ignore[arg-type]

        with self.assertRaises(ATSTypeError):
            SubProcessor(generator=valid_generator, scheme_builder=invalid_type)  # type: ignore[arg-type]

    def test_run_success_and_nested_logging(self) -> None:
        '''
            Verifies template generation and file logging.

            :exceptions: None.
        '''
        mock_logger: Mock = Mock(spec=ILogger)
        mock_generator: Mock = Mock(spec=IGeneratorManager)
        mock_generator.get_context.return_value = Mock(logger=mock_logger)
        mock_generator.generate.return_value = True
        mock_builder: Mock = Mock(spec=ISchemeBuilder)
        mock_builder.build.return_value = {}

        subprocessor: SubProcessor = SubProcessor(
            generator=mock_generator,
            scheme_builder=mock_builder
        )

        with TemporaryDirectory() as tmp_dir:
            with open(join(tmp_dir, 'README.md'), 'w', encoding='utf-8') as root_file:
                root_file.write('# root\n')

            sub_dir: str = join(tmp_dir, 'dbus_server')
            makedirs(sub_dir, exist_ok=True)
            with open(join(sub_dir, 'main.py'), 'w', encoding='utf-8') as nested_file:
                nested_file.write('# nested\n')

            result: Mapping[str, object] = subprocessor.run(
                params=ProjectSetup(
                    name='demo-dbus',
                    project_type=ProjectType.POSIX_PY.value,
                    role=DBusRole.BOTH.value,
                    bus=BusType.SYSTEM.value,
                    output=tmp_dir
                )
            )

        self.assertEqual(result['returncode'], 0)
        self.assertIn('demo-dbus', str(result['stdout']))
        self.assertGreaterEqual(mock_logger.write_log.call_count, 3)

    def test_run_real_templates(self) -> None:
        '''
            Verifies end-to-end generation across types and roles.

            :exceptions: None.
        '''
        bundle: GenDBusBundle = GenDBusBundleFactory.create_bundle()

        with TemporaryDirectory() as tmp_dir:
            for proj_type in ProjectType.values():
                out_dir: str = join(tmp_dir, proj_type)
                result: Mapping[str, object] = bundle.subprocessor.run(
                    params=ProjectSetup(
                        name='sample_svc',
                        project_type=proj_type,
                        role=DBusRole.BOTH.value,
                        bus=BusType.SESSION.value,
                        output=out_dir
                    )
                )
                self.assertEqual(result['returncode'], 0)
                self.assertTrue(exists(join(out_dir, 'dbus_server')))
                self.assertTrue(exists(join(out_dir, 'dbus_client')))
                self.assertTrue(
                    exists(join(out_dir, 'introspection', 'org.vroncevic.sample_svc.xml'))
                )

            cli_only: str = join(tmp_dir, 'cli_only')
            res_cli: Mapping[str, object] = bundle.subprocessor.run(
                params=ProjectSetup(
                    name='sample_svc',
                    project_type=ProjectType.POSIX_C.value,
                    role=DBusRole.CLIENT.value,
                    bus=BusType.SESSION.value,
                    output=cli_only
                )
            )
            self.assertEqual(res_cli['returncode'], 0)
            self.assertTrue(exists(join(cli_only, 'dbus_client')))
            self.assertFalse(exists(join(cli_only, 'dbus_server')))

    def test_run_failures(self) -> None:
        '''
            Verifies unsuccessful generation and invalid setup errors.

            :exceptions: None.
        '''
        mock_generator: Mock = Mock(spec=IGeneratorManager)
        mock_generator.get_context.return_value = Mock(logger=Mock(spec=ILogger))
        mock_generator.generate.return_value = False
        mock_builder: Mock = Mock(spec=ISchemeBuilder)
        mock_builder.build.return_value = {}

        subprocessor: SubProcessor = SubProcessor(
            generator=mock_generator,
            scheme_builder=mock_builder
        )

        failed: Mapping[str, object] = subprocessor.run(
            params=ProjectSetup(
                name='demo_dbus',
                project_type='posix_c',
                role='both',
                bus='session',
                output='./out'
            )
        )
        self.assertEqual(failed['returncode'], 1)
        self.assertIn('failed to generate demo_dbus', str(failed['stderr']))

        bad_type: Mapping[str, object] = subprocessor.run(
            params=ProjectSetup(
                name='demo_dbus',
                project_type='bad_type',
                role='both',
                bus='session',
                output='./out'
            )
        )
        self.assertEqual(bad_type['returncode'], 1)
        self.assertIn('unsupported project type', str(bad_type['stderr']))

        bad_role: Mapping[str, object] = subprocessor.run(
            params=ProjectSetup(
                name='demo_dbus',
                project_type='posix_c',
                role='bad_role',
                bus='session',
                output='./out'
            )
        )
        self.assertEqual(bad_role['returncode'], 1)
        self.assertIn('unsupported dbus role', str(bad_role['stderr']))

        bad_bus: Mapping[str, object] = subprocessor.run(
            params=ProjectSetup(
                name='demo_dbus',
                project_type='posix_c',
                role='both',
                bus='bad_bus',
                output='./out'
            )
        )
        self.assertEqual(bad_bus['returncode'], 1)
        self.assertIn('unsupported dbus bus', str(bad_bus['stderr']))

        invalid_none: object = None
        exc_result: Mapping[str, object] = subprocessor.run(params=invalid_none)  # type: ignore[arg-type]
        self.assertEqual(exc_result['returncode'], 1)

    def test_state_and_str(self) -> None:
        '''
            Verifies is_initialized and string representation.

            :exceptions: None.
        '''
        mock_generator: Mock = Mock(spec=IGeneratorManager)
        mock_generator.get_context.return_value = Mock(logger=Mock(spec=ILogger))
        mock_generator.is_initialized.return_value = True

        subprocessor: SubProcessor = SubProcessor(
            generator=mock_generator,
            scheme_builder=SchemeBuilder()
        )
        self.assertTrue(subprocessor.is_initialized())
        self.assertIsInstance(str(subprocessor), str)


if __name__ == '__main__':
    main()
