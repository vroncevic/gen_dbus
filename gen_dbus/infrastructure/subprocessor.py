# -*- coding: UTF-8 -*-

'''
Module
    subprocessor.py
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
    Defines SubProcessor adapter implementing ISubProcessor structurally.
'''

from __future__ import annotations

from collections.abc import Mapping
from datetime import date
from logging import INFO
from os import walk
from os.path import dirname, realpath, relpath
from typing import ClassVar

from ats_utilities.exceptions import ATSValueError
from ats_utilities.generation.data import GeneratorData
from ats_utilities.generation.imanager import IGeneratorManager
from ats_utilities.logger.ilogger import ILogger
from ats_utilities.utils.reflection import to_str
from ats_utilities.validation.check_type import istype
from ats_utilities.validation.check_value import not_none

from gen_dbus.core.model.bus_type import BusType
from gen_dbus.core.model.dbus_role import DBusRole
from gen_dbus.core.model.project_setup import ProjectSetup
from gen_dbus.core.model.project_type import ProjectType
from gen_dbus.infrastructure.ischeme_builder import ISchemeBuilder

__author__ = 'Vladimir Roncevic'
__copyright__ = 'Copyright (C) 2021 - 2026 Vladimir Roncevic <elektron.ronca@gmail.com>'
__credits__ = ['Vladimir Roncevic', 'Python Software Foundation']
__license__ = 'https://github.com/vroncevic/gen_dbus/blob/dev/LICENSE'
__version__ = '1.1.6'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Updated'


class SubProcessor:
    '''
        Defines class SubProcessor implementing ISubProcessor contract structurally.
        Adapter that generates D-Bus IPC project files from packaged templates.

        It defines:

            :attributes:
                | SCHEME_PATH - Relative path to scheme configuration JSON file.
                | TEMPLATES_PATH - Relative path to templates archive file.
                | C_BUS_SESSION - C/C++ libdbus session bus constant name.
                | C_BUS_SYSTEM - C/C++ libdbus system bus constant name.
                | PY_BUS_SESSION - Python dbus-fast session bus enum constant.
                | PY_BUS_SYSTEM - Python dbus-fast system bus enum constant.
                | _generator - Generator manager used to render project files.
                | _scheme_builder - Collaborator building role-filtered scheme.
                | _logger - Logger used to log operational messages.
            :methods:
                | __init__ - Initializes SubProcessor adapter.
                | run - Executes template generation for ProjectSetup.
                | is_initialized - Checks if the subprocessor is initialized.
                | __str__ - Returns SubProcessor string representation.
    '''

    SCHEME_PATH: ClassVar[str] = 'config/scheme.json'
    TEMPLATES_PATH: ClassVar[str] = 'config/templates.tgz'
    C_BUS_SESSION: ClassVar[str] = 'DBUS_BUS_SESSION'
    C_BUS_SYSTEM: ClassVar[str] = 'DBUS_BUS_SYSTEM'
    PY_BUS_SESSION: ClassVar[str] = 'SESSION'
    PY_BUS_SYSTEM: ClassVar[str] = 'SYSTEM'

    _generator: IGeneratorManager
    _scheme_builder: ISchemeBuilder
    _logger: ILogger

    def __init__(
        self,
        generator: IGeneratorManager,
        scheme_builder: ISchemeBuilder
    ) -> None:
        '''
            Initializes SubProcessor adapter.

            :param generator: Generator manager instance.
            :param scheme_builder: Role-aware scheme builder collaborator.
            :exceptions:
                | ATSValueError: If generator or scheme_builder is None.
                | ATSTypeError: If collaborators do not satisfy their protocols.
        '''
        ctx: str = 'subprocessor::init(...)'
        not_none(generator, ctx, 'the generator must be provided')
        istype(
            generator,
            IGeneratorManager,
            ctx,
            f'the generator must be an instance of {IGeneratorManager.__name__}'
        )
        not_none(scheme_builder, ctx, 'the scheme builder must be provided')
        istype(
            scheme_builder,
            ISchemeBuilder,
            ctx,
            f'the scheme builder must be an instance of {ISchemeBuilder.__name__}'
        )

        self._generator = generator
        self._scheme_builder = scheme_builder
        self._logger = generator.get_context().logger

    def run(self, *, params: ProjectSetup) -> Mapping[str, object]:
        '''
            Executes template generation for ProjectSetup.

            :param params: ProjectSetup containing project name, type, role, bus, and output.
            :return: Mapping with returncode, stdout, and stderr messages.
            :exceptions: None.
        '''
        project_name: str = 'unknown'

        try:
            ctx: str = 'subprocessor::run(...)'
            not_none(params, ctx, 'the params must be provided')
            istype(
                params,
                ProjectSetup,
                ctx,
                f'the params must be an instance of {ProjectSetup.__name__}'
            )

            project_name = params.name

            if params.project_type not in ProjectType.values():
                raise ATSValueError(ctx, f'unsupported project type {params.project_type}')

            if params.role not in DBusRole.values():
                raise ATSValueError(ctx, f'unsupported dbus role {params.role}')

            if params.bus not in BusType.values():
                raise ATSValueError(ctx, f'unsupported dbus bus {params.bus}')

            current_dir: str = dirname(realpath(__file__))
            clean_ident: str = project_name.replace('-', '_').lower()
            pascal_name: str = ''.join(
                word.capitalize() for word in clean_ident.split('_') if word
            )

            success: bool = self._generator.generate(
                data=GeneratorData(
                    archive_path=f'{current_dir}/{self.TEMPLATES_PATH}',
                    target_dir=params.output,
                    template_key=params.project_type,
                    scheme=self._scheme_builder.build(
                        scheme_path=f'{current_dir}/{self.SCHEME_PATH}',
                        project_type=params.project_type,
                        role=params.role
                    ),
                    template_values={
                        'project_name': clean_ident,
                        'PRO': project_name,
                        'PRO_LOWER': clean_ident,
                        'PRO_PASCAL': pascal_name,
                        'PRO_UPPER': clean_ident.upper(),
                        'BUS_TYPE': params.bus,
                        'C_BUS_CONST': (
                            self.C_BUS_SYSTEM
                            if params.bus == BusType.SYSTEM.value
                            else self.C_BUS_SESSION
                        ),
                        'PY_BUS_CONST': (
                            self.PY_BUS_SYSTEM
                            if params.bus == BusType.SYSTEM.value
                            else self.PY_BUS_SESSION
                        ),
                        'ROLE': params.role,
                        'YEAR': str(date.today().year),
                    }
                )
            )

            if success:
                self._logger.write_log(INFO, '    Generated files:')

                for root, _, files in walk(params.output):
                    for file in files:
                        rel_dir: str = relpath(root, params.output)

                        if rel_dir == '.':
                            self._logger.write_log(INFO, f'      {file}')
                        else:
                            self._logger.write_log(INFO, f'      {rel_dir}/{file}')

            return {
                'returncode': 0 if success else 1,
                'stdout': f'dbus project {project_name} successfully generated.' if success else '',
                'stderr': f'failed to generate {project_name} dbus project.' if not success else ''
            }

        except Exception as exc:
            return {
                'returncode': 1,
                'stdout': '',
                'stderr': f'failed to generate {project_name} dbus project {exc}'
            }

    def is_initialized(self) -> bool:
        '''
            Checks if the subprocessor is initialized.

            :return: True if collaborators are initialized, False otherwise.
            :exceptions: None.
        '''
        return self._generator.is_initialized() and self._scheme_builder.is_initialized()

    def __str__(self) -> str:
        '''
            Returns SubProcessor string representation.

            :return: String representation of SubProcessor.
            :exceptions: None.
        '''
        return to_str(self)
