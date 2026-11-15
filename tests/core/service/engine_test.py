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
    Defines unit tests for Service application use-case orchestrator.
'''

from __future__ import annotations

from collections.abc import Mapping
from unittest import TestCase, main
from unittest.mock import Mock

from gen_dbus.core.model.project_setup import ProjectSetup
from gen_dbus.core.service.engine import Service
from gen_dbus.core.service.isubprocessor import ISubProcessor

__author__ = 'Vladimir Roncevic'
__copyright__ = 'Copyright (C) 2021 - 2026 Vladimir Roncevic <elektron.ronca@gmail.com>'
__credits__ = ['Vladimir Roncevic', 'Python Software Foundation']
__license__ = 'https://github.com/vroncevic/gen_dbus/blob/dev/LICENSE'
__version__ = '1.1.6'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Updated'


class TestService(TestCase):
    '''
        Defines unit tests for Service application use-case orchestrator.

        It defines:

            :methods:
                | test_init_validation - Verifies constructor validates subprocessor.
                | test_execute_and_validation - Verifies execute delegation and argument checks.
                | test_is_initialized - Verifies initialization state delegation.
    '''

    def test_init_validation(self) -> None:
        '''
            Verifies constructor validates subprocessor.

            :exceptions: None.
        '''
        invalid_none: object = None
        invalid_type: object = 'invalid'

        with self.assertRaises(ValueError):
            Service(subprocessor=invalid_none)  # type: ignore[arg-type]

        with self.assertRaises(TypeError):
            Service(subprocessor=invalid_type)  # type: ignore[arg-type]

    def test_execute_and_validation(self) -> None:
        '''
            Verifies execute delegation and argument checks.

            :exceptions: None.
        '''
        mock_subprocessor: Mock = Mock(spec=ISubProcessor)
        mock_subprocessor.run.return_value = {'returncode': 0, 'stdout': 'done', 'stderr': ''}
        service: Service = Service(subprocessor=mock_subprocessor)

        setup: ProjectSetup = ProjectSetup(
            name='demo_dbus',
            project_type='posix_py',
            role='both',
            bus='session',
            output='./out'
        )
        result: Mapping[str, object] = service.execute(params=setup)
        self.assertEqual(result['returncode'], 0)
        mock_subprocessor.run.assert_called_once_with(params=setup)

        invalid_none: object = None
        invalid_type: object = 'invalid'

        with self.assertRaises(ValueError):
            service.execute(params=invalid_none)  # type: ignore[arg-type]

        with self.assertRaises(TypeError):
            service.execute(params=invalid_type)  # type: ignore[arg-type]

    def test_is_initialized(self) -> None:
        '''
            Verifies initialization state delegation.

            :exceptions: None.
        '''
        mock_subprocessor: Mock = Mock(spec=ISubProcessor)
        mock_subprocessor.is_initialized.return_value = True
        service: Service = Service(subprocessor=mock_subprocessor)
        self.assertTrue(service.is_initialized())


if __name__ == '__main__':
    main()
