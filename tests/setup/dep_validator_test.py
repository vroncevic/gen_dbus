# -*- coding: UTF-8 -*-

'''
Module
    dep_validator_test.py
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
    Defines unit tests for GenDBusBundleDependenciesValidator class.
'''

from __future__ import annotations

from unittest import TestCase, main

from ats_utilities.exceptions import ATSTypeError, ATSValueError

from gen_dbus.setup.bundle import GenDBusBundle
from gen_dbus.setup.dep_validator import GenDBusBundleDependenciesValidator
from gen_dbus.setup.dependencies import GenDBusBundleDependencies
from gen_dbus.setup.factory import GenDBusBundleFactory

__author__ = 'Vladimir Roncevic'
__copyright__ = 'Copyright (C) 2021 - 2026 Vladimir Roncevic <elektron.ronca@gmail.com>'
__credits__ = ['Vladimir Roncevic', 'Python Software Foundation']
__license__ = 'https://github.com/vroncevic/gen_dbus/blob/dev/LICENSE'
__version__ = '1.1.6'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Updated'


class TestGenDBusBundleDependenciesValidator(TestCase):
    '''
        Defines unit tests for GenDBusBundleDependenciesValidator class.

        It defines:

            :methods:
                | test_validate_and_is_valid - Verifies valid and invalid GenDBus bundle dependencies.
    '''

    def test_validate_and_is_valid(self) -> None:
        '''
            Verifies valid and invalid GenDBus bundle dependencies.

            :exceptions: None.
        '''
        bundle: GenDBusBundle = GenDBusBundleFactory.create_bundle()
        valid: GenDBusBundleDependencies = GenDBusBundleDependencies(
            base=bundle.base,
            service=bundle.service,
            subprocessor=bundle.subprocessor,
            cli=bundle.cli
        )
        self.assertTrue(GenDBusBundleDependenciesValidator.is_valid(valid))

        invalid_none: object = None
        invalid_type: object = 'invalid'
        self.assertFalse(GenDBusBundleDependenciesValidator.is_valid(invalid_none))  # type: ignore[arg-type]

        with self.assertRaises(ATSTypeError):
            GenDBusBundleDependenciesValidator.validate(invalid_type)  # type: ignore[arg-type]

        with self.assertRaises(ATSValueError):
            GenDBusBundleDependenciesValidator.validate({})  # type: ignore[typeddict-item]


if __name__ == '__main__':
    main()
