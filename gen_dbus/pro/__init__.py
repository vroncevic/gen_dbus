# -*- coding: UTF-8 -*-

'''
 Module
     __init__.py
 Copyright
     Copyright (C) 2021 Vladimir Roncevic <elektron.ronca@gmail.com>
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
     Defined class DBus with attribute(s) and method(s).
     Generate module file generator_test.py by template and parameters.
'''

import sys
from os.path import dirname, realpath

try:
    from gen_dbus.pro.config import ProConfig
    from gen_dbus.pro.config.pro_name import ProName
    from gen_dbus.pro.read_template import ReadTemplate
    from gen_dbus.pro.write_template import WriteTemplate
    from ats_utilities.checker import ATSChecker
    from ats_utilities.config_io.base_check import FileChecking
    from ats_utilities.console_io.error import error_message
    from ats_utilities.console_io.verbose import verbose_message
    from ats_utilities.config_io.yaml.yaml2object import Yaml2Object
    from ats_utilities.exceptions.ats_type_error import ATSTypeError
    from ats_utilities.exceptions.ats_bad_call_error import ATSBadCallError
except ImportError as ats_error_message:
    MESSAGE = '\n{0}\n{1}\n'.format(__file__, ats_error_message)
    sys.exit(MESSAGE)  # Force close python ATS ##############################

__author__ = 'Vladimir Roncevic'
__copyright__ = 'Copyright 2021, https://vroncevic.github.io/gen_dbus'
__credits__ = ['Vladimir Roncevic']
__license__ = 'https://github.com/vroncevic/gen_dbus/blob/dev/LICENSE'
__version__ = '1.0.0'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Updated'


class DBus(FileChecking, ProConfig, ProName):
    '''
        Defined class DBus with attribute(s) and method(s).
        Generate module file generator_test.py by template and parameters.
        It defines:

            :attributes:
                | GEN_VERBOSE - console text indicator for process-phase.
                | PRO_STRUCTURE - template/project structure.
                | __reader - reader API.
                | __writer - writer API.
            :methods:
                | __init__ - initial constructor.
                | get_reader - getter for template reader.
                | get_writer - getter for template writer.
                | gen_setup - generate module file setup.py.
                | __str__ - dunder method for DBus.
    '''

    GEN_VERBOSE = 'GEN_DBUS::PRO::DBUS'
    PRO_STRUCTURE = '/../conf/project.yaml'

    def __init__(self, verbose=False):
        '''
            Initial constructor.

            :param verbose: enable/disable verbose option.
            :type verbose: <bool>
            :exceptions: None
        '''
        FileChecking.__init__(self, verbose=verbose)
        ProConfig.__init__(self, verbose=verbose)
        ProName.__init__(self, verbose=verbose)
        verbose_message(DBus.GEN_VERBOSE, verbose, 'init setup')
        self.__reader = ReadTemplate(verbose=verbose)
        self.__writer = WriteTemplate(verbose=verbose)
        project_structure = '{0}{1}'.format(
            dirname(realpath(__file__)), DBus.PRO_STRUCTURE
        )
        self.check_path(project_structure, verbose=verbose)
        self.check_mode('r', verbose=verbose)
        self.check_format(project_structure, 'yaml', verbose=verbose)
        if self.is_file_ok():
            yml2obj = Yaml2Object(project_structure)
            self.__config = yml2obj.read_configuration()

    def get_reader(self):
        '''
            Getter for template reader.

            :return: template reader object.
            :rtype: <ReadTemplate>
            :exceptions: None
        '''
        return self.__reader

    def get_writer(self):
        '''
            Getter for template writer.

            :return: template writer object.
            :rtype: <WriteTemplate>
            :exceptions: None
        '''
        return self.__writer

    def select_pro_type(self, verbose=False):
        '''
            Select form type.

            :param verbose: enable/disable verbose option.
            :type verbose: <bool>
            :return: project template/module selected | None.
            :rtype: <dict>, <dict> | <NoneType>, <NoneType>
            :exceptions: None
        '''
        template_selected, module_selected = None, None
        if bool(self.__config):
            types = self.__config['templates']
            modules = self.__config['modules']
            pro_types_len = len(types)
            for index, pro_type in enumerate(types):
                print(
                    '{0} {1}'.format(index + 1, list(pro_type.keys())[0])
                )
                verbose_message(
                    DBus.GEN_VERBOSE, verbose,
                    'to be processed template', list(pro_type.keys())[0]
                )
            while True:
                input_type = input(' select project type: ')
                options = range(1, pro_types_len + 1, 1)
                try:
                    if int(input_type) in list(options):
                        template_selected = types[int(input_type) - 1]
                        module_selected = modules[int(input_type) - 1]
                        break
                    else:
                        raise ValueError
                except ValueError:
                    error_message(
                        DBus.GEN_VERBOSE, 'not an appropriate choice'
                    )
            verbose_message(
                DBus.GEN_VERBOSE, verbose, 'selected', template_selected
            )
        return template_selected, module_selected

    def gen_setup(self, pro_name, verbose=False):
        '''
            Generate module generator_test.py.

            :param pro_name: project name.
            :type pro_name: <str>
            :param verbose: enable/disable verbose option.
            :type verbose: <bool>
            :return: boolean status, True (success) | False.
            :rtype: <bool>
            :exceptions: ATSTypeError | ATSBadCallError
        '''
        checker, error, status = ATSChecker(), None, False
        error, status = checker.check_params([
            ('str:pro_name', pro_name)
        ])
        if status == ATSChecker.TYPE_ERROR:
            raise ATSTypeError(error)
        if status == ATSChecker.VALUE_ERROR:
            raise ATSBadCallError(error)
        status, setup_content = False, None
        templates, modules = self.select_pro_type(verbose=verbose)
        verbose_message(
            DBus.GEN_VERBOSE, verbose, 'generating project', pro_name
        )
        if bool(templates) and bool(modules):
            if 'cancel' not in templates or 'cancel' not in modules:
                setup_content = self.__reader.read(
                    templates, modules, verbose=verbose
                )
                if setup_content:
                    status = self.__writer.write(
                        setup_content, pro_name, verbose=verbose
                    )
            else:
                status = True
        return status

    def __str__(self):
        '''
            Dunder method for DBus.

            :return: object in a human-readable format.
            :rtype: <str>
            :exceptions: None
        '''
        return '{0} ({1}, {2}, {3}, {4}, {5})'.format(
            self.__class__.__name__, FileChecking.__str__(self),
            ProConfig.__str__(self), ProName.__str__(self),
            str(self.__reader), str(self.__writer)
        )
