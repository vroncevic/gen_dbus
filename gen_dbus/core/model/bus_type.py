# -*- coding: UTF-8 -*-

'''
Module
    bus_type.py
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
    Defines BusType enumeration for supported D-Bus message buses.
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


class BusType(StrEnum):
    '''
        Defines supported D-Bus message bus types.

        It defines:

            :attributes:
                | SESSION - Per-user D-Bus session bus.
                | SYSTEM - System-wide D-Bus system bus.
            :methods:
                | values - Returns tuple of all supported D-Bus bus type values.
    '''

    SESSION = 'session'
    SYSTEM = 'system'

    @classmethod
    def values(cls) -> tuple[str, ...]:
        '''
            Returns tuple of all supported D-Bus bus type string values.

            :return: Immutable tuple of D-Bus bus type values.
            :exceptions: None.
        '''
        return tuple(member.value for member in cls)
