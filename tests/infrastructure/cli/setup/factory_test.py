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
    Defines unit tests for CLIBundleFactory class.
'''

from __future__ import annotations

from unittest import TestCase, main
from unittest.mock import Mock

from ats_utilities.option.imanager import IOptionManager

from gen_dbus.core.service.iservice import IService
from gen_dbus.infrastructure.cli.setup.bundle import CLIBundle
from gen_dbus.infrastructure.cli.setup.factory import CLIBundleFactory
from gen_dbus.infrastructure.cli.setup.options import CLIBundleOptions

__author__ = 'Vladimir Roncevic'
__copyright__ = 'Copyright (C) 2021 - 2026 Vladimir Roncevic <elektron.ronca@gmail.com>'
__credits__ = ['Vladimir Roncevic', 'Python Software Foundation']
__license__ = 'https://github.com/vroncevic/gen_dbus/blob/dev/LICENSE'
__version__ = '1.1.6'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Updated'


class TestCLIBundleFactory(TestCase):
    '''
        Defines unit tests for CLIBundleFactory class.

        It defines:

            :methods:
                | test_create_bundle_and_version - Verifies CLI bundle creation and version string.
    '''

    def test_create_bundle_and_version(self) -> None:
        '''
            Verifies CLI bundle creation and version string.

            :exceptions: None.
        '''
        bundle: CLIBundle = CLIBundleFactory.create_bundle(
            options=CLIBundleOptions(
                service=Mock(spec=IService),
                parser=Mock(spec=IOptionManager)
            )
        )
        self.assertIsInstance(bundle, CLIBundle)
        self.assertEqual(len(bundle.commands), 1)
        self.assertEqual(CLIBundleFactory.get_version(), '1.1.6')


if __name__ == '__main__':
    main()
