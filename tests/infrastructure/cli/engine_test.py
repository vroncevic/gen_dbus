# -*- coding: UTF-8 -*-

'''
Module
    engine_test.py
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
    Defines unit tests for CLI inbound adapter.
'''

from __future__ import annotations

from collections.abc import Mapping
from unittest import TestCase, main
from unittest.mock import Mock

from ats_utilities.exceptions import ATSRuntimeError, ATSValueError
from ats_utilities.option.imanager import IOptionManager

from gen_dbus.core.service.iservice import IService
from gen_dbus.infrastructure.cli.engine import CLI
from gen_dbus.infrastructure.cli.setup.factory import CLIBundleFactory
from gen_dbus.infrastructure.cli.setup.options import CLIBundleOptions

__author__ = 'Vladimir Roncevic'
__copyright__ = 'Copyright (C) 2021 - 2026 Vladimir Roncevic <elektron.ronca@gmail.com>'
__credits__ = ['Vladimir Roncevic', 'Python Software Foundation']
__license__ = 'https://github.com/vroncevic/gen_dbus/blob/dev/LICENSE'
__version__ = '1.1.6'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Updated'


class TestCLI(TestCase):
    '''
        Defines unit tests for CLI inbound adapter.

        It defines:

            :methods:
                | test_init_validation - Verifies constructor validates CLIBundle.
                | test_run_branches_and_accessors - Verifies dispatch, unknown command, exceptions, and str.
    '''

    def test_init_validation(self) -> None:
        '''
            Verifies constructor validates CLIBundle.

            :exceptions: None.
        '''
        invalid_none: object = None
        with self.assertRaises(ATSValueError):
            CLI(bundle=invalid_none)  # type: ignore[arg-type]

    def test_run_branches_and_accessors(self) -> None:
        '''
            Verifies dispatch, unknown command, exceptions, and str.

            :exceptions: None.
        '''
        mock_service: Mock = Mock(spec=IService)
        mock_service.is_initialized.return_value = True
        mock_service.execute.return_value = {'returncode': 0, 'stdout': 'generated', 'stderr': ''}

        mock_parser: Mock = Mock(spec=IOptionManager)
        mock_parser.parse_command.return_value = (
            'create',
            {'name': 'svc', 'type': 'posix_c', 'role': 'both', 'bus': 'session', 'output': './'}
        )

        cli: CLI = CLI(
            CLIBundleFactory.create_bundle(
                options=CLIBundleOptions(service=mock_service, parser=mock_parser)
            )
        )
        ok_res: Mapping[str, object] = cli.run()
        self.assertEqual(ok_res['returncode'], 0)

        mock_parser.parse_command.return_value = ('unknown', {})
        missing_res: Mapping[str, object] = cli.run()
        self.assertEqual(missing_res['returncode'], 1)
        self.assertIn('command not found', str(missing_res['stderr']))

        mock_parser.parse_command.side_effect = ATSRuntimeError('ctx', 'parse error')
        err_res: Mapping[str, object] = cli.run()
        self.assertEqual(err_res['returncode'], 1)

        self.assertTrue(cli.is_initialized())
        self.assertIsInstance(str(cli), str)


if __name__ == '__main__':
    main()
