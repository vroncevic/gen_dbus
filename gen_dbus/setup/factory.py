# -*- coding: UTF-8 -*-

'''
Module
    factory.py
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
    Factory for creating the GenDBusBundle.
'''

from __future__ import annotations

from os.path import abspath, dirname, join
from typing import ClassVar

from ats_utilities.base.setup.bundle import BaseBundle
from ats_utilities.base.setup.factory import BaseBundleFactory
from ats_utilities.base.setup.options import BaseBundleOptions
from ats_utilities.context.bundle import ContextBundle
from ats_utilities.context.factory import ContextBundleFactory

from gen_dbus.core.service.engine import Service
from gen_dbus.infrastructure.cli.engine import CLI
from gen_dbus.infrastructure.cli.setup.bundle import CLIBundle
from gen_dbus.infrastructure.cli.setup.factory import CLIBundleFactory
from gen_dbus.infrastructure.cli.setup.options import CLIBundleOptions
from gen_dbus.infrastructure.scheme_builder import SchemeBuilder
from gen_dbus.infrastructure.subprocessor import SubProcessor
from gen_dbus.setup.bundle import GenDBusBundle
from gen_dbus.setup.dependencies import GenDBusBundleDependencies
from gen_dbus.setup.keys import GenDBusBundleKeys
from gen_dbus.setup.opt_validator import GenDBusBundleOptionsValidator
from gen_dbus.setup.options import GenDBusBundleOptions
from gen_dbus.setup.registry import GenDBusBundleRegistry

__author__ = 'Vladimir Roncevic'
__copyright__ = 'Copyright (C) 2021 - 2026 Vladimir Roncevic <elektron.ronca@gmail.com>'
__credits__ = ['Vladimir Roncevic', 'Python Software Foundation']
__license__ = 'https://github.com/vroncevic/gen_dbus/blob/dev/LICENSE'
__version__ = '1.1.6'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Updated'


class GenDBusBundleFactory:
    '''
        Factory for creating the GenDBusBundle.

        It defines:

            :attributes:
                | DEFAULT_INFO_FILE - Default path to the gen_dbus info file.
            :methods:
                | create_bundle - Creates GenDBusBundle with optional pre-configured options.
                | get_version - Returns the factory version.
    '''

    DEFAULT_INFO_FILE: ClassVar[str] = join(
        dirname(dirname(abspath(__file__))), 'infrastructure', 'config', 'gen_dbus.cfg'
    )

    @classmethod
    def create_bundle(cls, options: GenDBusBundleOptions | None = None) -> GenDBusBundle:
        '''
            Creates GenDBusBundle with optional pre-configured options.

            :param options: Pre-configured options for the GenDBus bundle.
            :return: Validated GenDBusBundle instance.
            :exceptions:
                | ATSValueError: If options, dependencies, or bundle values are invalid.
                | ATSTypeError: If options, dependencies, or bundle types are invalid.
        '''
        if options is not None:
            GenDBusBundleOptionsValidator.validate(options)

        info_file: str = options[GenDBusBundleKeys.OPTION_INFO_FILE] if options else cls.DEFAULT_INFO_FILE

        context_bundle: ContextBundle = ContextBundleFactory.create_bundle()
        base_bundle: BaseBundle = BaseBundleFactory.create_bundle(
            options=BaseBundleOptions(
                info_file=info_file,
                use_generator=True,
                context_bundle=context_bundle
            )
        )

        subprocessor: SubProcessor = SubProcessor(
            generator=base_bundle.generation_manager,
            scheme_builder=SchemeBuilder()
        )
        service: Service = Service(subprocessor=subprocessor)

        cli_bundle: CLIBundle = CLIBundleFactory.create_bundle(
            options=CLIBundleOptions(
                service=service,
                parser=base_bundle.option_manager
            )
        )
        cli: CLI = CLI(cli_bundle)

        return GenDBusBundleRegistry.create_bundle(
            dependencies=GenDBusBundleDependencies(
                base=base_bundle,
                service=service,
                subprocessor=subprocessor,
                cli=cli
            )
        )

    @classmethod
    def get_version(cls) -> str:
        '''
            Returns the factory version.

            :return: Factory version string.
            :exceptions: None.
        '''
        return __version__
