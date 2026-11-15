# -*- coding: UTF-8 -*-

'''
Module
    definition.py
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
    Defines CommandDefinition class for CLI create command metadata.
'''

from __future__ import annotations

from collections.abc import Sequence
from typing import ClassVar

from ats_utilities.option.command.data import OptionData
from ats_utilities.utils.reflection import to_str

from gen_dbus.core.model.bus_type import BusType
from gen_dbus.core.model.dbus_role import DBusRole
from gen_dbus.core.model.project_type import ProjectType

__author__ = 'Vladimir Roncevic'
__copyright__ = 'Copyright (C) 2021 - 2026 Vladimir Roncevic <elektron.ronca@gmail.com>'
__credits__ = ['Vladimir Roncevic', 'Python Software Foundation']
__license__ = 'https://github.com/vroncevic/gen_dbus/blob/dev/LICENSE'
__version__ = '1.1.6'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Updated'


class CommandDefinition:
    '''
        Defines class CommandDefinition implementing ICommandDefinition contract structurally.
        CLI subcommand metadata definition for D-Bus project generation.

        It defines:

            :attributes:
                | COMMAND_NAME - CLI subcommand name.
                | HELP_TEXT - CLI subcommand help description.
                | DEFAULT_NAME - Default D-Bus project name option value.
                | DEFAULT_TYPE - Default D-Bus project template type value.
                | DEFAULT_ROLE - Default D-Bus generation role value.
                | DEFAULT_BUS - Default D-Bus message bus type value.
                | DEFAULT_OUTPUT - Default output directory option value.
            :methods:
                | name - Returns the command name.
                | help_text - Returns the command help text.
                | options - Returns the sequence of command options.
                | __str__ - Returns CommandDefinition string representation.
    '''

    COMMAND_NAME: ClassVar[str] = 'create'
    HELP_TEXT: ClassVar[str] = 'Generate D-Bus IPC project files'
    DEFAULT_NAME: ClassVar[str] = 'dbus_service'
    DEFAULT_TYPE: ClassVar[str] = ProjectType.POSIX_PY.value
    DEFAULT_ROLE: ClassVar[str] = DBusRole.BOTH.value
    DEFAULT_BUS: ClassVar[str] = BusType.SESSION.value
    DEFAULT_OUTPUT: ClassVar[str] = './'

    @property
    def name(self) -> str:
        '''
            Returns the command name.

            :return: Command name string.
            :exceptions: None.
        '''
        return self.COMMAND_NAME

    @property
    def help_text(self) -> str:
        '''
            Returns the command help text.

            :return: Command help text string.
            :exceptions: None.
        '''
        return self.HELP_TEXT

    @property
    def options(self) -> Sequence[OptionData]:
        '''
            Returns the command options.

            :return: Sequence of OptionData definitions.
            :exceptions: None.
        '''
        return (
            OptionData(
                name='--name',
                help_text='D-Bus project name',
                action=None,
                default=self.DEFAULT_NAME,
                required=True,
                choices=None,
                nargs=None
            ),
            OptionData(
                name='--type',
                help_text='D-Bus template type (posix_c, posix_cxx, posix_py)',
                action=None,
                default=self.DEFAULT_TYPE,
                required=True,
                choices=ProjectType.values(),
                nargs=None
            ),
            OptionData(
                name='--role',
                help_text='D-Bus endpoint role (both, client, server)',
                action=None,
                default=self.DEFAULT_ROLE,
                required=False,
                choices=DBusRole.values(),
                nargs=None
            ),
            OptionData(
                name='--bus',
                help_text='Target D-Bus message bus (session, system)',
                action=None,
                default=self.DEFAULT_BUS,
                required=False,
                choices=BusType.values(),
                nargs=None
            ),
            OptionData(
                name='--output',
                help_text='Path to the output directory',
                action=None,
                default=self.DEFAULT_OUTPUT,
                required=False,
                choices=None,
                nargs=None
            ),
        )

    def __str__(self) -> str:
        '''
            Returns CommandDefinition string representation.

            :return: String representation of CommandDefinition.
            :exceptions: None.
        '''
        return to_str(self)
