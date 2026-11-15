# -*- coding: UTF-8 -*-

'''
Module
    ischeme_builder.py
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
    Defines structural interface ISchemeBuilder for role-aware scheme assembly.
'''

from __future__ import annotations

from typing import Protocol, runtime_checkable

__author__ = 'Vladimir Roncevic'
__copyright__ = 'Copyright (C) 2021 - 2026 Vladimir Roncevic <elektron.ronca@gmail.com>'
__credits__ = ['Vladimir Roncevic', 'Python Software Foundation']
__license__ = 'https://github.com/vroncevic/gen_dbus/blob/dev/LICENSE'
__version__ = '1.1.6'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Updated'


@runtime_checkable
class ISchemeBuilder(Protocol):
    '''
        Defines structural interface ISchemeBuilder for scheme assembly.

        It defines:

            :methods:
                | build - Builds role-filtered template scheme mapping.
                | is_initialized - Checks if the scheme builder is initialized.
                | __str__ - Returns string representation of scheme builder.
    '''

    def build(
        self,
        *,
        scheme_path: str,
        project_type: str,
        role: str
    ) -> dict[str, object]:
        '''
            Builds role-filtered template scheme mapping from JSON file.

            :param scheme_path: Path to base scheme JSON file.
            :param project_type: Selected template key.
            :param role: Selected D-Bus generation role.
            :return: Resolved scheme configuration dictionary.
        '''

    def is_initialized(self) -> bool:
        '''
            Checks if the scheme builder is initialized.

            :return: True if initialized, False otherwise.
        '''

    def __str__(self) -> str:
        '''
            Returns string representation of scheme builder.

            :return: String representation.
        '''
