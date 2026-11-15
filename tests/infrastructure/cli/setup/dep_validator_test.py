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
    Defines unit tests for CLIBundleDependenciesValidator class.
'''

from __future__ import annotations

from unittest import TestCase, main
from unittest.mock import Mock

from ats_utilities.exceptions import ATSTypeError, ATSValueError
from ats_utilities.option.imanager import IOptionManager

from gen_dbus.core.service.iservice import IService
from gen_dbus.infrastructure.cli.setup.dep_validator import CLIBundleDependenciesValidator
from gen_dbus.infrastructure.cli.setup.dependencies import CLIBundleDependencies

__author__ = 'Vladimir Roncevic'
__copyright__ = 'Copyright (C) 2021 - 2026 Vladimir Roncevic <elektron.ronca@gmail.com>'
__credits__ = ['Vladimir Roncevic', 'Python Software Foundation']
__license__ = 'https://github.com/vroncevic/gen_dbus/blob/dev/LICENSE'
__version__ = '1.1.6'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Updated'


class TestCLIBundleDependenciesValidator(TestCase):
    '''
        Defines unit tests for CLIBundleDependenciesValidator class.

        It defines:

            :methods:
                | test_validate_and_is_valid - Verifies valid and invalid CLI bundle dependencies.
    '''

    def test_validate_and_is_valid(self) -> None:
        '''
            Verifies valid and invalid CLI bundle dependencies.

            :exceptions: None.
        '''
        valid: CLIBundleDependencies = CLIBundleDependencies(
            service=Mock(spec=IService),
            parser=Mock(spec=IOptionManager),
            commands=()
        )
        self.assertTrue(CLIBundleDependenciesValidator.is_valid(valid))

        invalid_none: object = None
        invalid_type: object = 'invalid'
        self.assertFalse(CLIBundleDependenciesValidator.is_valid(invalid_none))  # type: ignore[arg-type]

        with self.assertRaises(ATSTypeError):
            CLIBundleDependenciesValidator.validate(invalid_type)  # type: ignore[arg-type]

        with self.assertRaises(ATSValueError):
            CLIBundleDependenciesValidator.validate({})  # type: ignore[typeddict-item]


if __name__ == '__main__':
    main()
