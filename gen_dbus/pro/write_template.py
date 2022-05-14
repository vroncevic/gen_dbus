# -*- coding: UTF-8 -*-

'''
 Module
     write_template.py
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
     Defined class WriteTemplate with attribute(s) and method(s).
     Created API for write operation of template content.
'''

import sys
from os import getcwd, chmod, mkdir
from os.path import exists, isdir
from datetime import date
from string import Template

try:
    from ats_utilities.checker import ATSChecker
    from ats_utilities.config_io.base_check import FileChecking
    from ats_utilities.console_io.verbose import verbose_message
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


class WriteTemplate(FileChecking):
    '''
        Defined class WriteTemplate with attribute(s) and method(s).
        Created API for write operation of template content.
        It defines:

            :attributes:
                | GEN_VERBOSE - console text indicator for process-phase.
                | __setup - setup file path.
            :methods:
                | __init__ - initial constructor.
                | get_setup - getter for setup file object.
                | write - write a template content to a file generator_test.py.
                | __str__ - dunder method for WriteTemplate.
    '''

    GEN_VERBOSE = 'GEN_DBUS::PRO::WRITE_TEMPLATE'

    def __init__(self, verbose=False):
        '''
            Initial constructor.

            :param verbose: enable/disable verbose option.
            :type verbose: <bool>
            :exceptions: None
        '''
        FileChecking.__init__(self, verbose=verbose)
        verbose_message(WriteTemplate.GEN_VERBOSE, verbose, 'init writer')
        self.__setup = None

    def get_setup(self):
        '''
            Getter for setup file object.

            :return: setup file path | None.
            :rtype: <str> | <NoneType>
        '''
        return self.__setup

    def write(self, setup_content, pro_name, verbose=False):
        '''
            Write setup content to file generator_test.py.

            :param setup_content: template content.
            :type setup_content: <dict>
            :param pro_name: parameter package name.
            :type pro_name: <str>
            :param verbose: enable/disable verbose option.
            :type verbose: <bool>
            :return: boolean status, True (success) | False.
            :rtype: <bool>
            :exception: ATSTypeError | ATSBadCallError
        '''
        checker, error, status = ATSChecker(), None, False
        error, status = checker.check_params([
            ('dict:setup_content', setup_content), ('str:pro_name', pro_name)
        ])
        if status == ATSChecker.TYPE_ERROR:
            raise ATSTypeError(error)
        if status == ATSChecker.VALUE_ERROR:
            raise ATSBadCallError(error)
        template = None
        self.__setup = '{0}/{1}'.format(getcwd(), pro_name)
        verbose_message(WriteTemplate.GEN_VERBOSE, verbose, 'write', pro_name)
        if not exists(self.__setup) or not isdir(self.__setup):
            mkdir(self.__setup)
            for entity_dir in list(setup_content.keys()):
                mkdir('{0}/{1}'.format(self.__setup, entity_dir))
                mkdir('{0}/{1}/src'.format(self.__setup, entity_dir))
                mkdir('{0}/{1}/po'.format(self.__setup, entity_dir))
        else:
            return False
        package, statuses = {
            'PRO': '{0}'.format(pro_name),
            'YEAR': '{0}'.format(date.today().year)
        }, []
        for entity in list(setup_content.keys()):
            for module, content in setup_content[entity].items():
                template = Template(content)
                if template:
                    template_file = '{0}/{1}/{2}'.format(
                        self.__setup, entity, module
                    )
                    with open(template_file, 'w') as setup_file:
                        setup_file.write(template.substitute(package))
                        chmod(template_file, 0o666)
                        statuses.append(True)            
        return all(statuses)

    def __str__(self):
        '''
            Dunder method for WriteTemplate.

            :return: object in a human-readable format.
            :rtype: <str>
            :exceptions: None
        '''
        return '{0} ({1}, {2})'.format(
            self.__class__.__name__, FileChecking.__str__(self),
            str(self.__setup)
        )
