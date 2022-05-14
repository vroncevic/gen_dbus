Generate DBus
--------------

☯️ **gen_dbus** is tool for generation of dbus modules.

Developed in 🐍 `python <https://www.python.org/>`_ code.

The README is used to introduce the modules and provide instructions on
how to install the modules, any machine dependencies it may have and any
other information that should be provided before the modules are installed.

|python package| |github issues| |documentation status| |github contributors|

.. |python package| image:: https://img.shields.io/github/workflow/status/vroncevic/gen_dbus/gen_dbus_python_checker?style=flat&label=gen_dbus%20python%20checker
   :target: https://img.shields.io/github/workflow/status/vroncevic/gen_dbus/gen_dbus_python_checker

.. |github issues| image:: https://img.shields.io/github/workflow/status/vroncevic/gen_dbus/gen_dbus_package_checker?style=flat&label=gen_dbus%20package%20checker
   :target: https://img.shields.io/github/workflow/status/vroncevic/gen_dbus/gen_dbus_package_checker

.. |github contributors| image:: https://img.shields.io/github/contributors/vroncevic/gen_dbus.svg
   :target: https://github.com/vroncevic/gen_dbus/graphs/contributors

.. |documentation status| image:: https://readthedocs.org/projects/gen-autoconf/badge/?version=latest
   :target: https://readthedocs.org/projects/gen-autoconf/badge/?version=latest

.. toctree::
   :maxdepth: 4
   :caption: Contents

   self
   modules

Installation
-------------

|install python2 package| |install python3 package|

.. |install python2 package| image:: https://img.shields.io/github/workflow/status/vroncevic/gen_dbus/gen_dbus_python2_build?style=flat&label=gen_dbus%20python2%20build
   :target: https://img.shields.io/github/workflow/status/vroncevic/gen_dbus/gen_dbus_python2_build

.. |install python3 package| image:: https://img.shields.io/github/workflow/status/vroncevic/gen_dbus/gen_dbus_python3_build?style=flat&label=gen_dbus%20python3%20build
   :target: https://img.shields.io/github/workflow/status/vroncevic/gen_dbus/gen_dbus_python3_build

Navigate to release `page`_ download and extract release archive.

.. _page: https://github.com/vroncevic/gen_dbus/releases

To install this set of modules type the following

.. code-block:: bash

    tar xvzf gen_dbus-x.y.z.tar.gz
    cd gen_dbus-x.y.z
    #python2
    pip install -r requirements.txt
    python setup.py install_lib
    python setup.py install_egg_info
    python setup.py install_data
    #python3
    pip3 install -r requirements.txt
    python3 setup.py install_lib
    python3 setup.py install_egg_info
    python3 setup.py install_data

You can use Docker to create image/container, or You can use pip to install

.. code-block:: bash

    #python2
    pip install gen_dbus
    #python3
    pip3 install gen_dbus

|github docker checker|

.. |github docker checker| image:: https://img.shields.io/github/workflow/status/vroncevic/gen_dbus/gen_dbus_docker_checker?style=flat&label=gen_dbus%20docker%20checker
   :target: https://img.shields.io/github/workflow/status/vroncevic/gen_dbus/gen_dbus_docker_checker

Dependencies
-------------

**gen_dbus** requires next modules and libraries

* `ats-utilities - Python App/Tool/Script Utilities <https://pypi.org/project/ats-utilities/>`_

Tool structure
------------------

**gen_dbus** is based on OOP

🧰 Code structure

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
    │   ├── config/
    │   │   ├── __init__.py
    │   │   └── pro_name.py
    │   ├── __init__.py
    │   ├── read_template.py
    │   └── write_template.py
    └── run/
        └── gen_dbus_run.py

Copyright and licence
----------------------

|license: gpl v3| |license: apache 2.0|

.. |license: gpl v3| image:: https://img.shields.io/badge/license-gplv3-blue.svg
   :target: https://www.gnu.org/licenses/gpl-3.0

.. |license: apache 2.0| image:: https://img.shields.io/badge/license-apache%202.0-blue.svg
   :target: https://opensource.org/licenses/apache-2.0

Copyright (C) 2021 by `vroncevic.github.io/gen_dbus <https://vroncevic.github.io/gen_dbus>`_

**gen_dbus** is free software; you can redistribute it and/or modify
it under the same terms as Python itself, either Python version 2.x/3.x or,
at your option, any later version of Python 3 you may have available.

🌎 🌍 🌏 Lets help and support PSF.

|python software foundation|

.. |python software foundation| image:: https://raw.githubusercontent.com/vroncevic/gen_dbus/dev/docs/psf-logo-alpha.png
   :target: https://www.python.org/psf/

|donate|

.. |donate| image:: https://www.paypalobjects.com/en_us/i/btn/btn_donatecc_lg.gif
   :target: https://psfmember.org/index.php?q=civicrm/contribute/transact&reset=1&id=2

Indices and tables
------------------

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`
