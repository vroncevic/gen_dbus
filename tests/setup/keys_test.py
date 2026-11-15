# -*- coding: UTF-8 -*-

'''
Module
    keys_test.py
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
    Defines unit tests for GenDBusBundleKeys class.
'''

from __future__ import annotations

from unittest import TestCase, main

from ats_utilities.base.setup.bundle import BaseBundle

from gen_dbus.core.service.iservice import IService
from gen_dbus.core.service.isubprocessor import ISubProcessor
from gen_dbus.infrastructure.cli.icli import ICLI
from gen_dbus.setup.keys import GenDBusBundleKeys

__author__ = 'Vladimir Roncevic'
__copyright__ = 'Copyright (C) 2021 - 2026 Vladimir Roncevic <elektron.ronca@gmail.com>'
__credits__ = ['Vladimir Roncevic', 'Python Software Foundation']
__license__ = 'https://github.com/vroncevic/gen_dbus/blob/dev/LICENSE'
__version__ = '1.1.6'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Updated'


class TestGenDBusBundleKeys(TestCase):
    '''
        Defines unit tests for GenDBusBundleKeys class.

        It defines:

            :methods:
                | test_mappings - Verifies dependency and option type mappings.
    '''

    def test_mappings(self) -> None:
        '''
            Verifies dependency and option type mappings.

            :exceptions: None.
        '''
        dep_map: dict[str, type] = dict(GenDBusBundleKeys.get_dependency_to_type())
        self.assertEqual(dep_map['base'], BaseBundle)
        self.assertEqual(dep_map['service'], IService)
        self.assertEqual(dep_map['subprocessor'], ISubProcessor)
        self.assertEqual(dep_map['cli'], ICLI)

        opt_map: dict[str, type] = dict(GenDBusBundleKeys.get_option_to_type())
        self.assertEqual(opt_map['info_file'], str)


if __name__ == '__main__':
    main()
