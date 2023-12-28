Generate DBus
--------------

**gen_dbus** is tool for generation of dbus modules.

Developed in `python <https://www.python.org/>`_ code.

The README is used to introduce the modules and provide instructions on
how to install the modules, any machine dependencies it may have and any
other information that should be provided before the modules are installed.

|gen_dbus python checker| |gen_dbus python package| |github issues| |documentation status| |github contributors|

.. |gen_dbus python checker| image:: https://github.com/vroncevic/gen_dbus/actions/workflows/gen_dbus_python_checker.yml/badge.svg
   :target: https://github.com/vroncevic/gen_dbus/actions/workflows/gen_dbus_python_checker.yml

.. |gen_dbus python package| image:: https://github.com/vroncevic/gen_dbus/actions/workflows/gen_dbus_package_checker.yml/badge.svg
   :target: https://github.com/vroncevic/gen_dbus/actions/workflows/gen_dbus_package.yml

.. |github issues| image:: https://img.shields.io/github/issues/vroncevic/gen_dbus.svg
   :target: https://github.com/vroncevic/gen_dbus/issues

.. |github contributors| image:: https://img.shields.io/github/contributors/vroncevic/gen_dbus.svg
   :target: https://github.com/vroncevic/gen_dbus/graphs/contributors

.. |documentation status| image:: https://readthedocs.org/projects/gen-dbus/badge/?version=latest
   :target: https://gen-dbus.readthedocs.io/en/latest/?badge=latest

.. toctree::
   :maxdepth: 4
   :caption: Contents

   self
   modules

Installation
-------------

|gen_dbus python3 build|

.. |gen_dbus python3 build| image:: https://github.com/vroncevic/gen_dbus/actions/workflows/gen_dbus_python3_build.yml/badge.svg
   :target: https://github.com/vroncevic/gen_dbus/actions/workflows/gen_dbus_python3_build.yml

Navigate to release `page`_ download and extract release archive.

.. _page: https://github.com/vroncevic/gen_dbus/releases

To install **gen_dbus** type the following

.. code-block:: bash

    tar xvzf gen-dbus-x.y.z.tar.gz
    cd gen-dbus-x.y.z/
    # python3
    wget https://bootstrap.pypa.io/get-pip.py
    python3 get-pip.py 
    python3 -m pip install --upgrade setuptools
    python3 -m pip install --upgrade pip
    python3 -m pip install --upgrade build
    pip3 install -r requirements.txt
    python3 -m build --no-isolation --wheel
    pip3 install ./dist/gen_dbus-*-py3-none-any.whl
    rm -f get-pip.py
    chmod 755 /usr/local/lib/python3.10/dist-packages/usr/local/bin/gen_dbus_run.py
    ln -s /usr/local/lib/python3.10/dist-packages/usr/local/bin/gen_dbus_run.py /usr/local/bin/gen_dbus_run.py

You can use Docker to create image/container, or You can use pip to install

.. code-block:: bash

    #python3
    pip3 install gen_dbus

Dependencies
-------------

**gen_dbus** requires next modules and libraries

* `ats-utilities - Python App/Tool/Script Utilities <https://pypi.org/project/ats-utilities/>`_

Tool structure
------------------

**gen_dbus** is based on OOP

Code structure

.. code-block:: bash

    gen_dbus/
        ├── conf/
        │   ├── gen_dbus.cfg
        │   ├── gen_dbus.logo
        │   ├── gen_dbus_util.cfg
        │   ├── project.yaml
        │   └── template/
        │       ├── posix_c/
        │       │   ├── dbus_client/
        │       │   │   ├── AUTHORS.template
        │       │   │   ├── autogen.template
        │       │   │   ├── ChangeLog.template
        │       │   │   ├── configure.template
        │       │   │   ├── COPYING.template
        │       │   │   ├── Makefile.template
        │       │   │   ├── NEWS.template
        │       │   │   ├── README.template
        │       │   │   └── src/
        │       │   │       ├── main.template
        │       │   │       └── Makefile.template
        │       │   └── dbus_server/
        │       │       ├── AUTHORS.template
        │       │       ├── autogen.template
        │       │       ├── ChangeLog.template
        │       │       ├── configure.template
        │       │       ├── COPYING.template
        │       │       ├── Makefile.template
        │       │       ├── NEWS.template
        │       │       ├── README.template
        │       │       └── src/
        │       │           ├── main.template
        │       │           └── Makefile.template
        │       ├── posix_cxx/
        │       │   ├── dbus_client/
        │       │   │   ├── AUTHORS.template
        │       │   │   ├── autogen.template
        │       │   │   ├── ChangeLog.template
        │       │   │   ├── configure.template
        │       │   │   ├── COPYING.template
        │       │   │   ├── Makefile.template
        │       │   │   ├── NEWS.template
        │       │   │   ├── po/
        │       │   │   │   ├── ChangeLog.template
        │       │   │   │   ├── LINGUAS.template
        │       │   │   │   └── POTFILES.template
        │       │   │   ├── README.template
        │       │   │   └── src/
        │       │   │       ├── main.template
        │       │   │       └── Makefile.template
        │       │   └── dbus_server/
        │       │       ├── AUTHORS.template
        │       │       ├── autogen.template
        │       │       ├── ChangeLog.template
        │       │       ├── configure.template
        │       │       ├── COPYING.template
        │       │       ├── Makefile.template
        │       │       ├── NEWS.template
        │       │       ├── po/
        │       │       │   ├── ChangeLog.template
        │       │       │   ├── LINGUAS.template
        │       │       │   └── POTFILES.template
        │       │       ├── README.template
        │       │       └── src/
        │       │           ├── main.template
        │       │           └── Makefile.template
        │       └── posix_py/
        │           ├── dbus_client/
        │           │   ├── AUTHORS.template
        │           │   ├── autogen.template
        │           │   ├── ChangeLog.template
        │           │   ├── configure.template
        │           │   ├── COPYING.template
        │           │   ├── Makefile.template
        │           │   ├── NEWS.template
        │           │   ├── README.template
        │           │   └── src/
        │           │       ├── dbus_client.template
        │           │       └── Makefile.template
        │           └── dbus_server/
        │               ├── AUTHORS.template
        │               ├── autogen.template
        │               ├── ChangeLog.template
        │               ├── configure.template
        │               ├── COPYING.template
        │               ├── Makefile.template
        │               ├── NEWS.template
        │               ├── README.template
        │               └── src/
        │                   ├── dbus_server.template
        │                   └── Makefile.template
        ├── __init__.py
        ├── log/
        │   └── gen_dbus.log
        ├── pro/
        │   ├── __init__.py
        │   ├── read_template.py
        │   └── write_template.py
        └── run/
            └── gen_dbus_run.py
        
        23 directories, 76 files

Copyright and licence
----------------------

|license: gpl v3| |license: apache 2.0|

.. |license: gpl v3| image:: https://img.shields.io/badge/license-gplv3-blue.svg
   :target: https://www.gnu.org/licenses/gpl-3.0

.. |license: apache 2.0| image:: https://img.shields.io/badge/license-apache%202.0-blue.svg
   :target: https://opensource.org/licenses/apache-2.0

Copyright (C) 2021 - 2024 by `vroncevic.github.io/gen_dbus <https://vroncevic.github.io/gen_dbus>`_

**gen_dbus** is free software; you can redistribute it and/or modify
it under the same terms as Python itself, either Python version 3.x or,
at your option, any later version of Python 3 you may have available.

Lets help and support PSF.

|python software foundation|

.. |python software foundation| image:: https://raw.githubusercontent.com/vroncevic/gen_dbus/dev/docs/psf-logo-alpha.png
   :target: https://www.python.org/psf/

|donate|

.. |donate| image:: https://www.paypalobjects.com/en_us/i/btn/btn_donatecc_lg.gif
   :target: https://www.python.org/psf/donations/

Indices and tables
------------------

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
