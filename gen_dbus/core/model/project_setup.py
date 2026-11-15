# -*- coding: UTF-8 -*-

'''
Module
    project_setup.py
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
    Defines domain model for a D-Bus project generation setup.
'''

from __future__ import annotations

from dataclasses import dataclass

__author__ = 'Vladimir Roncevic'
__copyright__ = 'Copyright (C) 2021 - 2026 Vladimir Roncevic <elektron.ronca@gmail.com>'
__credits__ = ['Vladimir Roncevic', 'Python Software Foundation']
__license__ = 'https://github.com/vroncevic/gen_dbus/blob/dev/LICENSE'
__version__ = '1.1.6'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Updated'


@dataclass(frozen=True, slots=True, kw_only=True)
class ProjectSetup:
    '''
        Defines domain model for a D-Bus project generation setup.

        It defines:

            :attributes:
                | name - Name of the D-Bus project to generate.
                | project_type - Type of the D-Bus project template to generate.
                | role - D-Bus generation role (both, client, or server).
                | bus - Target D-Bus message bus (session or system).
                | output - Target directory path for generated project files.
            :methods:
                | to_dict - Converts ProjectSetup instance to a dictionary.
    '''

    name: str
    project_type: str
    role: str
    bus: str
    output: str

    def to_dict(self) -> dict[str, object]:
        '''
            Converts ProjectSetup instance to a dictionary.

            :return: Dictionary representation of ProjectSetup.
            :exceptions: None.
        '''
        return {
            'name': self.name,
            'project_type': self.project_type,
            'role': self.role,
            'bus': self.bus,
            'output': self.output,
        }
