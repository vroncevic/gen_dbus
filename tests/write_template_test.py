# -*- coding: UTF-8 -*-

'''
Module
    write_template_test.py
Copyright
    Copyright (C) 2021 - 2024 Vladimir Roncevic <elektron.ronca@gmail.com>
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
    Defines class WriteTemplateTestCase with attribute(s) and method(s).
    Creates test cases for checking functionalities of WriteTemplate.
Execute
    python3 -m unittest -v write_template_test
'''

import sys
from typing import Any, Tuple, Dict, List
from os.path import dirname, realpath
from unittest import TestCase, main

try:
    from ats_utilities.config_io.yaml.yaml2object import Yaml2Object
    from ats_utilities.exceptions.ats_type_error import ATSTypeError
    from ats_utilities.exceptions.ats_value_error import ATSValueError
    from gen_dbus.pro.read_template import ReadTemplate
    from gen_dbus.pro.write_template import WriteTemplate
except ImportError as test_error_message:
    # Force close python test #################################################
    sys.exit(f'\n{__file__}\n{test_error_message}\n')

__author__ = 'Vladimir Roncevic'
__copyright__ = '(C) 2024, https://vroncevic.github.io/gen_dbus'
__credits__: List[str] = ['Vladimir Roncevic', 'Python Software Foundation']
__license__ = 'https://github.com/vroncevic/gen_dbus/blob/dev/LICENSE'
__version__ = '1.1.3'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Updated'


class WriteTemplateTestCase(TestCase):
    '''
        Defines class WriteTemplateTestCase with attribute(s) and method(s).
        Creates test cases for checking functionalities of WriteTemplate.
        WriteTemplate unit tests.

        It defines:

            :attributes:
                | None
            :methods:
                | setUp - call before test case.
                | tearDown - call after test case.
                | test_write_template_create - Test write templates create.
                | test_write_template_empty - Test write templates empty.
                | test_write_template_none - Test write templates None.
                | test_write_template - Test write templates.
    '''

    def setUp(self) -> None:
        '''Call before test case.'''

    def tearDown(self) -> None:
        '''Call after test case.'''

    def test_write_template_create(self) -> None:
        '''Test write templates create'''
        template = WriteTemplate()
        self.assertIsNotNone(template)

    def test_write_template_empty(self) -> None:
        '''Test write templates empty'''
        template = WriteTemplate()
        templates: List[Tuple[Dict[str, str], Dict[str, str]]] = []
        with self.assertRaises(ATSValueError):
            self.assertFalse(
                template.write(templates, 'empty_simple_test', 'posix_c')
            )

    def test_write_template_none(self) -> None:
        '''Test write templates None'''
        template = WriteTemplate()
        with self.assertRaises(ATSTypeError):
            self.assertFalse(
                template.write(
                    None, 'none_simple_test', 'posix_c'  # type: ignore
                )
            )

    def test_write_template(self) -> None:
        '''Test write templates'''
        template_read = ReadTemplate()
        current_dir: str = dirname(realpath(__file__))
        pro_structure: str = f'{current_dir}/../gen_dbus/conf/project.yaml'
        yml2obj = Yaml2Object(pro_structure)
        template_cfg: Dict[Any, Any] = yml2obj.read_configuration()
        template_write = WriteTemplate()
        pro_setup: List[
            Tuple[Dict[str, str], Dict[str, str]]
        ] = template_read.read(template_cfg, 'posix_c')
        self.assertTrue(
            template_write.write(pro_setup, 'new_simple_test', 'posix_c')
        )


if __name__ == '__main__':
    main()
