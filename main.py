# -*- coding: UTF-8 -*-

'''
Module
    main.py
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
    Main entry point of the gen_dbus D-Bus project generator tool.
'''

from __future__ import annotations

from sys import exit as sys_exit

from gen_dbus.engine import GenDBus
from gen_dbus.setup.factory import GenDBusBundleFactory

__author__ = 'Vladimir Roncevic'
__copyright__ = 'Copyright (C) 2021 - 2026 Vladimir Roncevic <elektron.ronca@gmail.com>'
__credits__ = ['Vladimir Roncevic', 'Python Software Foundation']
__license__ = 'https://github.com/vroncevic/gen_dbus/blob/dev/LICENSE'
__version__ = '1.1.6'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Updated'


def main() -> bool:
    '''
        Bootstraps and runs gen_dbus with required adapters and configuration.

        :return: True if successful, False otherwise.
        :exceptions: None.
    '''
    tool: GenDBus = GenDBus(GenDBusBundleFactory.create_bundle())
    return tool.process()


if __name__ == '__main__':
    sys_exit(0 if main() else 1)
