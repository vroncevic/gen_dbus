# -*- coding: UTF-8 -*-

'''
Module
    factory_test.py
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
    Defines unit tests for GenDBusBundleFactory class.
'''

from __future__ import annotations

from unittest import TestCase, main

from gen_dbus.setup.bundle import GenDBusBundle
from gen_dbus.setup.factory import GenDBusBundleFactory
from gen_dbus.setup.options import GenDBusBundleOptions

__author__ = 'Vladimir Roncevic'
__copyright__ = 'Copyright (C) 2021 - 2026 Vladimir Roncevic <elektron.ronca@gmail.com>'
__credits__ = ['Vladimir Roncevic', 'Python Software Foundation']
__license__ = 'https://github.com/vroncevic/gen_dbus/blob/dev/LICENSE'
__version__ = '1.1.6'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Updated'


class TestGenDBusBundleFactory(TestCase):
    '''
        Defines unit tests for GenDBusBundleFactory class.

        It defines:

            :methods:
                | test_create_bundle_default_and_options - Verifies default and explicit options creation.
    '''

    def test_create_bundle_default_and_options(self) -> None:
        '''
            Verifies default and explicit options creation.

            :exceptions: None.
        '''
        default_bundle: GenDBusBundle = GenDBusBundleFactory.create_bundle()
        self.assertIsInstance(default_bundle, GenDBusBundle)

        explicit_bundle: GenDBusBundle = GenDBusBundleFactory.create_bundle(
            options=GenDBusBundleOptions(info_file=GenDBusBundleFactory.DEFAULT_INFO_FILE)
        )
        self.assertIsInstance(explicit_bundle, GenDBusBundle)
        self.assertEqual(GenDBusBundleFactory.get_version(), '1.1.6')


if __name__ == '__main__':
    main()
