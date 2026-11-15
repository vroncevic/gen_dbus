# -*- coding: UTF-8 -*-

'''
Module
    iexecutor_test.py
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
    Defines unit tests for ICommandExecutor structural protocol.
'''

from __future__ import annotations

from unittest import TestCase, main

from gen_dbus.infrastructure.command.definition import CommandDefinition
from gen_dbus.infrastructure.command.executor import CommandExecutor
from gen_dbus.infrastructure.command.iexecutor import ICommandExecutor

__author__ = 'Vladimir Roncevic'
__copyright__ = 'Copyright (C) 2021 - 2026 Vladimir Roncevic <elektron.ronca@gmail.com>'
__credits__ = ['Vladimir Roncevic', 'Python Software Foundation']
__license__ = 'https://github.com/vroncevic/gen_dbus/blob/dev/LICENSE'
__version__ = '1.1.6'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Updated'


class TestICommandExecutor(TestCase):
    '''
        Defines unit tests for ICommandExecutor structural protocol.

        It defines:

            :methods:
                | test_runtime_checkable_conformance - Verifies CommandExecutor satisfies ICommandExecutor.
                | test_non_conforming_object - Verifies arbitrary object does not satisfy ICommandExecutor.
    '''

    def test_runtime_checkable_conformance(self) -> None:
        '''
            Verifies CommandExecutor satisfies ICommandExecutor structurally.

            :exceptions: None.
        '''
        executor: CommandExecutor = CommandExecutor(definition=CommandDefinition())
        self.assertIsInstance(executor, ICommandExecutor)

    def test_non_conforming_object(self) -> None:
        '''
            Verifies arbitrary object does not satisfy ICommandExecutor.

            :exceptions: None.
        '''
        self.assertNotIsInstance(object(), ICommandExecutor)


if __name__ == '__main__':
    main()
