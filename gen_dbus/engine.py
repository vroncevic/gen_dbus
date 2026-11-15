# -*- coding: UTF-8 -*-

'''
Module
    engine.py
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
    Engine orchestrating initialization and execution of gen_dbus.
'''

from __future__ import annotations

from collections.abc import Mapping
from logging import ERROR, INFO
from sys import stdout

from ats_utilities.base.engine import Base
from ats_utilities.exceptions import ATSTypeError, ATSValueError
from ats_utilities.logger.ilogger import ILogger

from gen_dbus.infrastructure.cli.icli import ICLI
from gen_dbus.setup.bundle import GenDBusBundle
from gen_dbus.setup.validator import GenDBusBundleValidator

__author__ = 'Vladimir Roncevic'
__copyright__ = 'Copyright (C) 2021 - 2026 Vladimir Roncevic <elektron.ronca@gmail.com>'
__credits__ = ['Vladimir Roncevic', 'Python Software Foundation']
__license__ = 'https://github.com/vroncevic/gen_dbus/blob/dev/LICENSE'
__version__ = '1.1.6'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Updated'


class GenDBus(Base):
    '''
        Engine orchestrating initialization and execution of gen_dbus.

        It defines:

            :attributes:
                | _is_initialized - Flag indicating whether the engine is initialized.
                | _logger - Logger for operational messages during initialization and execution.
                | _cli - Inbound adapter for the command line interface.
            :methods:
                | __init__ - Initializes the GenDBus engine with validated bundle.
                | process - Processes the gen_dbus commands.
    '''

    _is_initialized: bool
    _logger: ILogger
    _cli: ICLI

    def __init__(self, bundle: GenDBusBundle) -> None:
        '''
            Initializes the GenDBus engine with validated bundle.

            :param bundle: GenDBus bundle containing adapters and services.
            :exceptions: None.
        '''
        self._is_initialized = False

        try:
            GenDBusBundleValidator.validate(bundle)
            super().__init__(bundle.base)

            self._is_initialized = False
            self._cli = bundle.cli
            self._is_initialized = all(
                component.is_initialized() for component in (
                    bundle.base.option_manager,
                    bundle.service,
                    bundle.subprocessor,
                    self._cli
                ) if component
            )

            self._logger = self.get_context().logger
            self._logger.write_log(INFO, '✅ gen_dbus: engine initialized successfully!')

        except (ATSValueError, ATSTypeError) as exc:
            stdout.write(f'❌ gen_dbus: {exc}!\n')

        except Exception as exc:
            stdout.write(f'❌ gen_dbus unexpected exception: {exc}!\n')

    def process(self, verbose: bool = False) -> bool:
        '''
            Processes the gen_dbus commands.

            :param verbose: Enable verbose output.
            :return: True if successful, False otherwise.
            :exceptions: None.
        '''
        _ = verbose

        try:
            if self.is_initialized():
                self._logger.write_log(INFO, '🔥 Starting execution command...')
                result: Mapping[str, object] = self._cli.run()
                self._logger.write_log(INFO, '✅ Execution finished!')

                if result.get('returncode') != 0:
                    self._logger.write_log(ERROR, f'❌ gen_dbus: {result.get("stderr") or "failed!"}')
                    return False

                self._logger.write_log(INFO, '✅ gen_dbus: done!')
                self._logger.write_log(INFO, '✅ gen_dbus: exiting successfully!')
                return True

            stdout.write('❌ gen_dbus: engine not initialized!\n')
            return False

        except (ATSValueError, ATSTypeError) as exc:
            stdout.write(f'❌ gen_dbus: {exc}!\n')
            return False

        except Exception as exc:
            stdout.write(f'❌ gen_dbus unexpected exception: {exc}!\n')
            return False
