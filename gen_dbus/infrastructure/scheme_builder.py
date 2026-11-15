# -*- coding: UTF-8 -*-

'''
Module
    scheme_builder.py
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
    Defines SchemeBuilder collaborator implementing ISchemeBuilder structurally.
'''

from __future__ import annotations

from collections.abc import Iterable, Mapping
from json import loads
from typing import ClassVar

from ats_utilities.utils.reflection import to_str
from ats_utilities.validation.check_type import istype
from ats_utilities.validation.check_value import not_none

from gen_dbus.core.model.dbus_role import DBusRole

__author__ = 'Vladimir Roncevic'
__copyright__ = 'Copyright (C) 2021 - 2026 Vladimir Roncevic <elektron.ronca@gmail.com>'
__credits__ = ['Vladimir Roncevic', 'Python Software Foundation']
__license__ = 'https://github.com/vroncevic/gen_dbus/blob/dev/LICENSE'
__version__ = '1.1.6'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Updated'


class SchemeBuilder:
    '''
        Defines class SchemeBuilder implementing ISchemeBuilder contract structurally.
        Loads scheme JSON metadata and applies D-Bus role exclusion filters.

        It defines:

            :attributes:
                | EXCLUDE_KEY - JSON key holding exclude glob patterns.
                | SERVER_DIR - Subdirectory excluded when role is client.
                | CLIENT_DIR - Subdirectory excluded when role is server.
            :methods:
                | build - Builds role-filtered template scheme dictionary.
                | is_initialized - Checks if the scheme builder is initialized.
                | __str__ - Returns SchemeBuilder string representation.
    '''

    EXCLUDE_KEY: ClassVar[str] = 'exclude'
    SERVER_DIR: ClassVar[str] = 'dbus_server'
    CLIENT_DIR: ClassVar[str] = 'dbus_client'

    def build(
        self,
        *,
        scheme_path: str,
        project_type: str,
        role: str
    ) -> dict[str, object]:
        '''
            Builds role-filtered template scheme dictionary from JSON file.

            :param scheme_path: Path to base scheme JSON file.
            :param project_type: Selected template key.
            :param role: Selected D-Bus generation role.
            :return: Resolved scheme configuration dictionary.
            :exceptions:
                | ATSValueError: If scheme_path, project_type, or role is None.
                | ATSTypeError: If scheme_path, project_type, or role is not str.
        '''
        ctx: str = 'scheme_builder::build(...)'
        not_none(scheme_path, ctx, 'the scheme path must be provided')
        istype(scheme_path, str, ctx, 'the scheme path must be an instance of str')
        not_none(project_type, ctx, 'the project type must be provided')
        istype(project_type, str, ctx, 'the project type must be an instance of str')
        not_none(role, ctx, 'the role must be provided')
        istype(role, str, ctx, 'the role must be an instance of str')

        with open(scheme_path, 'r', encoding='utf-8') as scheme_file:
            raw_data: object = loads(scheme_file.read())

        scheme_data: dict[str, object] = (
            {str(key): val for key, val in raw_data.items()}
            if isinstance(raw_data, Mapping) else {}
        )
        entry: object = scheme_data.get(project_type)

        if isinstance(entry, Mapping):
            type_config: dict[str, object] = {str(k): v for k, v in entry.items()}
            raw_excludes: object = type_config.get(self.EXCLUDE_KEY, [])
            excludes: list[str] = (
                [str(item) for item in raw_excludes]
                if isinstance(raw_excludes, Iterable) and not isinstance(raw_excludes, str)
                else []
            )

            match role:
                case DBusRole.CLIENT.value:
                    excludes.append(self.SERVER_DIR)
                case DBusRole.SERVER.value:
                    excludes.append(self.CLIENT_DIR)
                case _:
                    pass

            type_config[self.EXCLUDE_KEY] = excludes
            scheme_data[project_type] = type_config

        return scheme_data

    def is_initialized(self) -> bool:
        '''
            Checks if the scheme builder is initialized.

            :return: True as SchemeBuilder is stateless and ready.
            :exceptions: None.
        '''
        return True

    def __str__(self) -> str:
        '''
            Returns SchemeBuilder string representation.

            :return: String representation of SchemeBuilder.
            :exceptions: None.
        '''
        return to_str(self)
