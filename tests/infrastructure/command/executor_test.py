# -*- coding: UTF-8 -*-

'''
Module
    executor_test.py
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
    Defines unit tests for CommandExecutor class.
'''

from __future__ import annotations

from collections.abc import Mapping
from unittest import TestCase, main
from unittest.mock import Mock

from ats_utilities.exceptions import ATSTypeError, ATSValueError

from gen_dbus.core.model.project_setup import ProjectSetup
from gen_dbus.core.service.iservice import IService
from gen_dbus.infrastructure.command.definition import CommandDefinition
from gen_dbus.infrastructure.command.executor import CommandExecutor

__author__ = 'Vladimir Roncevic'
__copyright__ = 'Copyright (C) 2021 - 2026 Vladimir Roncevic <elektron.ronca@gmail.com>'
__credits__ = ['Vladimir Roncevic', 'Python Software Foundation']
__license__ = 'https://github.com/vroncevic/gen_dbus/blob/dev/LICENSE'
__version__ = '1.1.6'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Updated'


class TestCommandExecutor(TestCase):
    '''
        Defines unit tests for CommandExecutor class.

        It defines:

            :methods:
                | test_init_validation - Verifies constructor validates definition.
                | test_execute_and_accessors - Verifies execute branches, get_definition, and str.
    '''

    def test_init_validation(self) -> None:
        '''
            Verifies constructor validates definition.

            :exceptions: None.
        '''
        invalid_none: object = None
        invalid_type: object = 'invalid'

        with self.assertRaises(ATSValueError):
            CommandExecutor(definition=invalid_none)  # type: ignore[arg-type]

        with self.assertRaises(ATSTypeError):
            CommandExecutor(definition=invalid_type)  # type: ignore[arg-type]

    def test_execute_and_accessors(self) -> None:
        '''
            Verifies execute branches, get_definition, and str.

            :exceptions: None.
        '''
        definition: CommandDefinition = CommandDefinition()
        executor: CommandExecutor = CommandExecutor(definition=definition)

        uninit_service: Mock = Mock(spec=IService)
        uninit_service.is_initialized.return_value = False
        uninit_res: Mapping[str, object] = executor.execute(params={}, service=uninit_service)
        self.assertEqual(uninit_res['returncode'], 1)
        self.assertIn('service not initialized', str(uninit_res['stderr']))

        ok_service: Mock = Mock(spec=IService)
        ok_service.is_initialized.return_value = True
        ok_service.execute.return_value = {'returncode': 0, 'stdout': 'ok', 'stderr': ''}

        ok_res: Mapping[str, object] = executor.execute(
            params={
                'name': 'telemetry_svc',
                'type': 'posix_cxx',
                'role': 'server',
                'bus': 'system',
                'output': './out',
            },
            service=ok_service
        )
        self.assertEqual(ok_res['returncode'], 0)
        ok_service.execute.assert_called_once_with(
            params=ProjectSetup(
                name='telemetry_svc',
                project_type='posix_cxx',
                role='server',
                bus='system',
                output='./out'
            )
        )
        self.assertIs(executor.get_definition(), definition)
        self.assertIsInstance(str(executor), str)


if __name__ == '__main__':
    main()
