#!/usr/bin/env python
# -*- coding: UTF-8 -*-

'''
 Module
     setup.py
 Copyright
     Copyright (C) 2021 - 2024 Vladimir Roncevic <elektron.ronca@gmail.com>
     gen_dbus is free software: you can redistribute it and/or
     modify it under the terms of the GNU General Public License as published
     by the Free Software Foundation, either version 3 of the License, or
     (at your option) any later version.
     gen_dbus is distributed in the hope that it will be useful,
     but WITHOUT ANY WARRANTY; without even the implied warranty of
     MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.
     See the GNU General Public License for more details.
     You should have received a copy of the GNU General Public License along
     with this program. If not, see <http://www.gnu.org/licenses/>.
 Info
     Define setup for tool gen_dbus.
'''

from __future__ import print_function
from typing import List
from os.path import abspath, dirname, join
from setuptools import setup

__author__ = 'Vladimir Roncevic'
__copyright__ = '(C) 2024, https://vroncevic.github.io/gen_dbus'
__credits__: List[str] = ['Vladimir Roncevic', 'Python Software Foundation']
__license__ = 'https://github.com/vroncevic/gen_dbus/blob/dev/LICENSE'
__version__ = '1.1.0'
__maintainer__ = 'Vladimir Roncevic'
__email__ = 'elektron.ronca@gmail.com'
__status__ = 'Updated'

TOOL_DIR = 'gen_dbus/'
CONF, TEMPLATE, LOG = 'conf', 'conf/template', 'log'
POSIX_C = 'template/posix_c'
POSIX_CC = 'template/posix_cxx'
POSIX_PY = 'template/posix_py'
THIS_DIR, LONG_DESCRIPTION = abspath(dirname(__file__)), None
with open(join(THIS_DIR, 'README.md'), encoding='utf-8') as readme:
    LONG_DESCRIPTION = readme.read()
PROGRAMMING_LANG = 'Programming Language :: Python ::'
VERSIONS = ['2.7', '3', '3.2', '3.3', '3.4']
SUPPORTED_PY_VERSIONS = [
    '{0} {1}'.format(PROGRAMMING_LANG, VERSION) for VERSION in VERSIONS
]
LICENSE_PREFIX = 'License :: OSI Approved ::'
LICENSES = [
    'GNU Lesser General Public License v2 (LGPLv2)',
    'GNU Lesser General Public License v2 or later (LGPLv2+)',
    'GNU Lesser General Public License v3 (LGPLv3)',
    'GNU Lesser General Public License v3 or later (LGPLv3+)',
    'GNU Library or Lesser General Public License (LGPL)'
]
APPROVED_LICENSES = [
    '{0} {1}'.format(LICENSE_PREFIX, LICENSE) for LICENSE in LICENSES
]
PYP_CLASSIFIERS = SUPPORTED_PY_VERSIONS + APPROVED_LICENSES
setup(
    name='gen_dbus',
    version='1.1.0',
    description='Generating DBus modules',
    author='Vladimir Roncevic',
    author_email='elektron.ronca@gmail.com',
    url='https://vroncevic.github.io/gen_dbus',
    license='GPL 2021 Free software to use and distributed it.',
    long_description=LONG_DESCRIPTION,
    long_description_content_type='text/markdown',
    keywords='Unix, Linux, Development, DBus, Modules',
    platforms='POSIX',
    classifiers=PYP_CLASSIFIERS,
    packages=[
        'gen_dbus', 'gen_dbus.pro', 'gen_dbus.pro.config'
    ],
    install_requires=['ats-utilities'],
    package_data={
        'gen_dbus': [
            '{0}/{1}'.format(CONF, 'gen_dbus.logo'),
            '{0}/{1}'.format(CONF, 'gen_dbus.cfg'),
            '{0}/{1}'.format(CONF, 'gen_dbus_util.cfg'),
            '{0}/{1}'.format(CONF, 'project.yaml'),
            '{0}/{1}'.format(POSIX_C, 'posix_c/dbus_client/AUTHORS.template'),
            '{0}/{1}'.format(POSIX_C, 'posix_c/dbus_client/COPYING.template'),
            '{0}/{1}'.format(POSIX_C, 'posix_c/dbus_client/ChangeLog.template'),
            '{0}/{1}'.format(POSIX_C, 'posix_c/dbus_client/Makefile.template'),
            '{0}/{1}'.format(POSIX_C, 'posix_c/dbus_client/NEWS.template'),
            '{0}/{1}'.format(POSIX_C, 'posix_c/dbus_client/README.template'),
            '{0}/{1}'.format(POSIX_C, 'posix_c/dbus_client/autogen.template'),
            '{0}/{1}'.format(POSIX_C, 'posix_c/dbus_client/configure.template'),
            '{0}/{1}'.format(POSIX_C, 'posix_c/dbus_client/src/Makefile.template'),
            '{0}/{1}'.format(POSIX_C, 'posix_c/dbus_client/src/main.template'),
            '{0}/{1}'.format(POSIX_C, 'posix_c/dbus_server/AUTHORS.template'),
            '{0}/{1}'.format(POSIX_C, 'posix_c/dbus_server/COPYING.template'),
            '{0}/{1}'.format(POSIX_C, 'posix_c/dbus_server/ChangeLog.template'),
            '{0}/{1}'.format(POSIX_C, 'posix_c/dbus_server/Makefile.template'),
            '{0}/{1}'.format(POSIX_C, 'posix_c/dbus_server/NEWS.template'),
            '{0}/{1}'.format(POSIX_C, 'posix_c/dbus_server/README.template'),
            '{0}/{1}'.format(POSIX_C, 'posix_c/dbus_server/autogen.template'),
            '{0}/{1}'.format(POSIX_C, 'posix_c/dbus_server/configure.template'),
            '{0}/{1}'.format(POSIX_C, 'posix_c/dbus_server/src/Makefile.template'),
            '{0}/{1}'.format(POSIX_C, 'posix_c/dbus_server/src/main.template'),
            '{0}/{1}'.format(POSIX_CC, 'posix_cxx/dbus_client/AUTHORS.template'),
            '{0}/{1}'.format(POSIX_CC, 'posix_cxx/dbus_client/COPYING.template'),
            '{0}/{1}'.format(POSIX_CC, 'posix_cxx/dbus_client/ChangeLog.template'),
            '{0}/{1}'.format(POSIX_CC, 'posix_cxx/dbus_client/Makefile.template'),
            '{0}/{1}'.format(POSIX_CC, 'posix_cxx/dbus_client/NEWS.template'),
            '{0}/{1}'.format(POSIX_CC, 'posix_cxx/dbus_client/README.template'),
            '{0}/{1}'.format(POSIX_CC, 'posix_cxx/dbus_client/autogen.template'),
            '{0}/{1}'.format(POSIX_CC, 'posix_cxx/dbus_client/configure.template'),
            '{0}/{1}'.format(POSIX_CC, 'posix_cxx/dbus_client/po/ChangeLog.template'),
            '{0}/{1}'.format(POSIX_CC, 'posix_cxx/dbus_client/po/LINGUAS.template'),
            '{0}/{1}'.format(POSIX_CC, 'posix_cxx/dbus_client/po/POTFILES.template'),
            '{0}/{1}'.format(POSIX_CC, 'posix_cxx/dbus_client/src/Makefile.template'),
            '{0}/{1}'.format(POSIX_CC, 'posix_cxx/dbus_client/src/main.template'),
            '{0}/{1}'.format(POSIX_CC, 'posix_cxx/dbus_server/AUTHORS.template'),
            '{0}/{1}'.format(POSIX_CC, 'posix_cxx/dbus_server/COPYING.template'),
            '{0}/{1}'.format(POSIX_CC, 'posix_cxx/dbus_server/ChangeLog.template'),
            '{0}/{1}'.format(POSIX_CC, 'posix_cxx/dbus_server/Makefile.template'),
            '{0}/{1}'.format(POSIX_CC, 'posix_cxx/dbus_server/NEWS.template'),
            '{0}/{1}'.format(POSIX_CC, 'posix_cxx/dbus_server/README.template'),
            '{0}/{1}'.format(POSIX_CC, 'posix_cxx/dbus_server/autogen.template'),
            '{0}/{1}'.format(POSIX_CC, 'posix_cxx/dbus_server/configure.template'),
            '{0}/{1}'.format(POSIX_CC, 'posix_cxx/dbus_server/po/ChangeLog.template'),
            '{0}/{1}'.format(POSIX_CC, 'posix_cxx/dbus_server/po/LINGUAS.template'),
            '{0}/{1}'.format(POSIX_CC, 'posix_cxx/dbus_server/po/POTFILES.template'),
            '{0}/{1}'.format(POSIX_CC, 'posix_cxx/dbus_server/src/Makefile.template'),
            '{0}/{1}'.format(POSIX_CC, 'posix_cxx/dbus_server/src/main.template'),
            '{0}/{1}'.format(POSIX_PY, 'posix_py/dbus_client/AUTHORS.template'),
            '{0}/{1}'.format(POSIX_PY, 'posix_py/dbus_client/COPYING.template'),
            '{0}/{1}'.format(POSIX_PY, 'posix_py/dbus_client/ChangeLog.template'),
            '{0}/{1}'.format(POSIX_PY, 'posix_py/dbus_client/Makefile.template'),
            '{0}/{1}'.format(POSIX_PY, 'posix_py/dbus_client/NEWS.template'),
            '{0}/{1}'.format(POSIX_PY, 'posix_py/dbus_client/README.template'),
            '{0}/{1}'.format(POSIX_PY, 'posix_py/dbus_client/autogen.template'),
            '{0}/{1}'.format(POSIX_PY, 'posix_py/dbus_client/configure.template'),
            '{0}/{1}'.format(POSIX_PY, 'posix_py/dbus_client/src/Makefile.template'),
            '{0}/{1}'.format(POSIX_PY, 'posix_py/dbus_client/src/dbus_client.template'),
            '{0}/{1}'.format(POSIX_PY, 'posix_py/dbus_server/AUTHORS.template'),
            '{0}/{1}'.format(POSIX_PY, 'posix_py/dbus_server/COPYING.template'),
            '{0}/{1}'.format(POSIX_PY, 'posix_py/dbus_server/ChangeLog.template'),
            '{0}/{1}'.format(POSIX_PY, 'posix_py/dbus_server/Makefile.template'),
            '{0}/{1}'.format(POSIX_PY, 'posix_py/dbus_server/NEWS.template'),
            '{0}/{1}'.format(POSIX_PY, 'posix_py/dbus_server/README.template'),
            '{0}/{1}'.format(POSIX_PY, 'posix_py/dbus_server/autogen.template'),
            '{0}/{1}'.format(POSIX_PY, 'posix_py/dbus_server/configure.template'),
            '{0}/{1}'.format(POSIX_PY, 'posix_py/dbus_server/src/Makefile.template'),
            '{0}/{1}'.format(POSIX_PY, 'posix_py/dbus_server/src/dbus_server.template'),
            '{0}/{1}'.format(LOG, 'gen_dbus.log')
        ]
    },
    data_files=[(
        '/usr/local/bin/', [
            '{0}{1}'.format(TOOL_DIR, 'run/gen_dbus_run.py')
        ]
    )]
)
