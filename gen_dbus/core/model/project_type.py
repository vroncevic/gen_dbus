# -*- coding: UTF-8 -*-

'''
Module
    project_type.py
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
    Defines ProjectType enumeration for supported D-Bus project templates.
'''

from __future__ import annotations

from enum import StrEnum

__author__ = 'Vladimir Roncevic'
__copyright__ = 'Copyright (C) 2021 - 2026 Vladimir Roncevic <elektron.ronca@gmail.com>'
__credits__ = ['Vladimir Roncevic', 'Python Software Foundation']
__license__ = 'https://github.com/vroncevic/gen_dbus/blob/dev/LICENSE'
__version__ = '1.1.6'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Updated'


class ProjectType(StrEnum):
    '''
        Defines supported D-Bus project template types.

        It defines:

            :attributes:
                | POSIX_C - C11 libdbus-1 D-Bus project template.
                | POSIX_CXX - C++20 RAII libdbus-1 D-Bus project template.
                | POSIX_PY - Python 3.12+ Clean Architecture dbus-fast project template.
            :methods:
                | values - Returns tuple of all supported project type values.
    '''

    POSIX_C = 'posix_c'
    POSIX_CXX = 'posix_cxx'
    POSIX_PY = 'posix_py'

    @classmethod
    def values(cls) -> tuple[str, ...]:
        '''
            Returns tuple of all supported project type string values.

            :return: Immutable tuple of project type values.
            :exceptions: None.
        '''
        return tuple(member.value for member in cls)
