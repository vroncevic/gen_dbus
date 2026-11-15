# -*- coding: UTF-8 -*-

'''
Module
    registry.py
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
    Registry assembling and validating GenDBusBundle instances.
'''

from __future__ import annotations

from gen_dbus.setup.bundle import GenDBusBundle
from gen_dbus.setup.dep_validator import GenDBusBundleDependenciesValidator
from gen_dbus.setup.dependencies import GenDBusBundleDependencies
from gen_dbus.setup.keys import GenDBusBundleKeys
from gen_dbus.setup.validator import GenDBusBundleValidator

__author__ = 'Vladimir Roncevic'
__copyright__ = 'Copyright (C) 2021 - 2026 Vladimir Roncevic <elektron.ronca@gmail.com>'
__credits__ = ['Vladimir Roncevic', 'Python Software Foundation']
__license__ = 'https://github.com/vroncevic/gen_dbus/blob/dev/LICENSE'
__version__ = '1.1.6'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Updated'


class GenDBusBundleRegistry:
    '''
        Registry assembling and validating GenDBusBundle instances.

        It defines:

            :methods:
                | create_bundle - Creates a validated GenDBusBundle from dependencies.
                | get_version - Returns the registry version.
    '''

    @classmethod
    def create_bundle(cls, dependencies: GenDBusBundleDependencies) -> GenDBusBundle:
        '''
            Creates a validated GenDBusBundle from dependencies.

            :param dependencies: GenDBus bundle dependencies.
            :return: Validated GenDBusBundle instance.
            :exceptions:
                | ATSValueError: If dependencies or bundle values are missing.
                | ATSTypeError: If dependencies or bundle types are invalid.
        '''
        GenDBusBundleDependenciesValidator.validate(dependencies)

        bundle: GenDBusBundle = GenDBusBundle(
            base=dependencies[GenDBusBundleKeys.DEPENDENCY_BASE],
            service=dependencies[GenDBusBundleKeys.DEPENDENCY_SERVICE],
            subprocessor=dependencies[GenDBusBundleKeys.DEPENDENCY_SUBPROCESSOR],
            cli=dependencies[GenDBusBundleKeys.DEPENDENCY_CLI]
        )

        GenDBusBundleValidator.validate(bundle)

        return bundle

    @classmethod
    def get_version(cls) -> str:
        '''
            Returns the registry version.

            :return: Registry version string.
            :exceptions: None.
        '''
        return __version__
