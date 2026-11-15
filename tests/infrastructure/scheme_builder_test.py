# -*- coding: UTF-8 -*-

'''
Module
    scheme_builder_test.py
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
    Defines unit tests for SchemeBuilder collaborator.
'''

from __future__ import annotations

from collections.abc import Mapping
from json import dumps
from os.path import join
from tempfile import TemporaryDirectory
from unittest import TestCase, main

from ats_utilities.exceptions import ATSTypeError, ATSValueError

from gen_dbus.infrastructure.scheme_builder import SchemeBuilder

__author__ = 'Vladimir Roncevic'
__copyright__ = 'Copyright (C) 2021 - 2026 Vladimir Roncevic <elektron.ronca@gmail.com>'
__credits__ = ['Vladimir Roncevic', 'Python Software Foundation']
__license__ = 'https://github.com/vroncevic/gen_dbus/blob/dev/LICENSE'
__version__ = '1.1.6'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Updated'


class TestSchemeBuilder(TestCase):
    '''
        Defines unit tests for SchemeBuilder collaborator.

        It defines:

            :methods:
                | test_build_role_filters - Verifies role exclusion filters for both, client, and server.
                | test_build_json_fallbacks - Verifies malformed exclude lists, missing keys, and non-dict JSON.
                | test_validation_and_state - Verifies argument validation, state, and str.
    '''

    def test_build_role_filters(self) -> None:
        '''
            Verifies role exclusion filters for both, client, and server.

            :exceptions: None.
        '''
        builder: SchemeBuilder = SchemeBuilder()
        sample_scheme: dict[str, object] = {
            'posix_c': {
                'source_dir': 'posix_c_templates',
                'path_replacements': {'pro_placeholder': 'project_name'},
                'exclude': ['**/.git/**'],
            },
        }

        with TemporaryDirectory() as tmp_dir:
            scheme_file: str = join(tmp_dir, 'scheme.json')
            with open(scheme_file, 'w', encoding='utf-8') as out:
                out.write(dumps(sample_scheme))

            both_entry: object = builder.build(
                scheme_path=scheme_file, project_type='posix_c', role='both'
            )['posix_c']
            self.assertIsInstance(both_entry, Mapping)
            if isinstance(both_entry, Mapping):
                self.assertEqual(both_entry['exclude'], ['**/.git/**'])

            cli_entry: object = builder.build(
                scheme_path=scheme_file, project_type='posix_c', role='client'
            )['posix_c']
            if isinstance(cli_entry, Mapping):
                self.assertIn('dbus_server', list(cli_entry['exclude']))  # type: ignore[arg-type]

            srv_entry: object = builder.build(
                scheme_path=scheme_file, project_type='posix_c', role='server'
            )['posix_c']
            if isinstance(srv_entry, Mapping):
                self.assertIn('dbus_client', list(srv_entry['exclude']))  # type: ignore[arg-type]

    def test_build_json_fallbacks(self) -> None:
        '''
            Verifies malformed exclude lists, missing keys, and non-dict JSON.

            :exceptions: None.
        '''
        builder: SchemeBuilder = SchemeBuilder()
        sample_scheme: dict[str, object] = {
            'broken_excludes': {
                'source_dir': 'broken',
                'exclude': 'not_a_list',
            },
        }

        with TemporaryDirectory() as tmp_dir:
            scheme_file: str = join(tmp_dir, 'scheme.json')
            with open(scheme_file, 'w', encoding='utf-8') as out:
                out.write(dumps(sample_scheme))

            broken_entry: object = builder.build(
                scheme_path=scheme_file, project_type='broken_excludes', role='both'
            )['broken_excludes']
            if isinstance(broken_entry, Mapping):
                self.assertEqual(broken_entry['exclude'], [])

            missing_res: dict[str, object] = builder.build(
                scheme_path=scheme_file, project_type='unknown', role='both'
            )
            self.assertNotIn('unknown', missing_res)

            non_dict_file: str = join(tmp_dir, 'array.json')
            with open(non_dict_file, 'w', encoding='utf-8') as arr_out:
                arr_out.write('[]')
            self.assertEqual(
                builder.build(scheme_path=non_dict_file, project_type='posix_c', role='both'),
                {}
            )

    def test_validation_and_state(self) -> None:
        '''
            Verifies argument validation, state, and str.

            :exceptions: None.
        '''
        builder: SchemeBuilder = SchemeBuilder()
        invalid_none: object = None
        invalid_type: object = 123

        with self.assertRaises(ATSValueError):
            builder.build(scheme_path=invalid_none, project_type='posix_c', role='both')  # type: ignore[arg-type]

        with self.assertRaises(ATSTypeError):
            builder.build(scheme_path=invalid_type, project_type='posix_c', role='both')  # type: ignore[arg-type]

        with self.assertRaises(ATSValueError):
            builder.build(scheme_path='s.json', project_type=invalid_none, role='both')  # type: ignore[arg-type]

        with self.assertRaises(ATSTypeError):
            builder.build(scheme_path='s.json', project_type=invalid_type, role='both')  # type: ignore[arg-type]

        with self.assertRaises(ATSValueError):
            builder.build(scheme_path='s.json', project_type='posix_c', role=invalid_none)  # type: ignore[arg-type]

        with self.assertRaises(ATSTypeError):
            builder.build(scheme_path='s.json', project_type='posix_c', role=invalid_type)  # type: ignore[arg-type]

        self.assertTrue(builder.is_initialized())
        self.assertIsInstance(str(builder), str)


if __name__ == '__main__':
    main()
