Generate D-Bus
--------------

**gen_dbus** is a Clean Architecture Python generator tool for creating production-grade D-Bus IPC projects in C11, C++20, and Python 3.12+.

Developed in `python <https://www.python.org/>`_ code.

The README is used to introduce the modules and provide instructions on
how to install the modules, any machine dependencies it may have and any
other information that should be provided before the modules are installed.

|gen_dbus python checker| |gen_dbus python package| |gen_dbus interface checker| |gen_dbus isp checker| |gen_dbus srp checker| |github issues| |documentation status| |github contributors|

.. |gen_dbus python checker| image:: https://github.com/vroncevic/gen_dbus/actions/workflows/gen_dbus_python_checker.yml/badge.svg
   :target: https://github.com/vroncevic/gen_dbus/actions/workflows/gen_dbus_python_checker.yml

.. |gen_dbus python package| image:: https://github.com/vroncevic/gen_dbus/actions/workflows/gen_dbus_package_checker.yml/badge.svg
   :target: https://github.com/vroncevic/gen_dbus/actions/workflows/gen_dbus_package_checker.yml

.. |gen_dbus interface checker| image:: https://github.com/vroncevic/gen_dbus/actions/workflows/gen_dbus_interface_checker.yml/badge.svg
   :target: https://github.com/vroncevic/gen_dbus/actions/workflows/gen_dbus_interface_checker.yml

.. |gen_dbus isp checker| image:: https://github.com/vroncevic/gen_dbus/actions/workflows/gen_dbus_isp_checker.yml/badge.svg
   :target: https://github.com/vroncevic/gen_dbus/actions/workflows/gen_dbus_isp_checker.yml

.. |gen_dbus srp checker| image:: https://github.com/vroncevic/gen_dbus/actions/workflows/gen_dbus_srp_checker.yml/badge.svg
   :target: https://github.com/vroncevic/gen_dbus/actions/workflows/gen_dbus_srp_checker.yml

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

🚀 Installation
---------------

|gen_dbus python3 build|

.. |gen_dbus python3 build| image:: https://github.com/vroncevic/gen_dbus/actions/workflows/gen_dbus_python3_build.yml/badge.svg
   :target: https://github.com/vroncevic/gen_dbus/actions/workflows/gen_dbus_python3_build.yml

Navigate to release `page`_ download and extract release archive.

.. _page: https://github.com/vroncevic/gen_dbus/releases

To install **gen_dbus** type the following

.. code-block:: bash

    tar xvzf gen-dbus-x.y.z.tar.gz
    cd gen-dbus-x.y.z/
    python3 -m pip install --upgrade setuptools pip build
    pip3 install -r requirements.txt
    python3 -m build --no-isolation --wheel
    pip3 install ./dist/gen_dbus-*-py3-none-any.whl

You can use Docker to create image/container, or You can use pip to install

.. code-block:: bash

    pip3 install gen-dbus

📦 Dependencies
---------------

**gen_dbus** requires next modules and libraries

* `ats-utilities - Python App/Tool/Script Utilities <https://pypi.org/project/ats-utilities/>`_

📁 Tool structure
-----------------

**gen_dbus** is based on Clean / Hexagonal Architecture and SOLID principles:

Code structure

.. code-block:: bash

    gen_dbus/
         ├── core/
         │   ├── __init__.py
         │   ├── model/
         │   │   ├── bus_type.py
         │   │   ├── dbus_role.py
         │   │   ├── __init__.py
         │   │   ├── project_setup.py
         │   │   └── project_type.py
         │   └── service/
         │       ├── engine.py
         │       ├── __init__.py
         │       ├── iservice.py
         │       └── isubprocessor.py
         ├── engine.py
         ├── infrastructure/
         │   ├── cli/
         │   │   ├── engine.py
         │   │   ├── icli.py
         │   │   ├── __init__.py
         │   │   └── setup/
         │   │       ├── bundle.py
         │   │       ├── dep_validator.py
         │   │       ├── dependencies.py
         │   │       ├── factory.py
         │   │       ├── __init__.py
         │   │       ├── keys.py
         │   │       ├── opt_validator.py
         │   │       ├── options.py
         │   │       ├── registry.py
         │   │       └── validator.py
         │   ├── command/
         │   │   ├── bundle.py
         │   │   ├── definition.py
         │   │   ├── executor.py
         │   │   ├── idefinition.py
         │   │   ├── iexecutor.py
         │   │   └── __init__.py
         │   ├── config/
         │   │   ├── gen_dbus.cfg
         │   │   ├── gen_dbus.logo
         │   │   ├── scheme.json
         │   │   └── templates.tgz
         │   ├── __init__.py
         │   ├── ischeme_builder.py
         │   ├── scheme_builder.py
         │   └── subprocessor.py
         ├── __init__.py
         ├── py.typed
         └── setup/
             ├── bundle.py
             ├── dep_validator.py
             ├── dependencies.py
             ├── factory.py
             ├── __init__.py
             ├── keys.py
             ├── opt_validator.py
             ├── options.py
             ├── registry.py
             └── validator.py

     10 directories, 50 files

✨ Features
-----------

* Generates production-ready, wire-compatible D-Bus IPC projects across 3 stacks: ``posix_c`` (C11 ``libdbus-1``), ``posix_cxx`` (C++20 RAII ``libdbus-1``), and ``posix_py`` (Python 3.12+ Clean Architecture ``dbus-fast``).
* Complete D-Bus Object Model out of the box: Method Calls (``Ping``, ``SetStatus``), Signals (``StatusChanged``), Properties (``Status``, ``CallCount``, ``PropertiesChanged``), and Introspection XML.
* Supports endpoint role filtering (``--role {both,client,server}``) and bus selection (``--bus {session,system}``).
* Strict SOLID & Hexagonal Architecture with structural ``Protocol`` interfaces, 10.00/10 ``pylint`` score, and 100% unit test coverage.

📊 Code coverage
----------------

.. csv-table:: Code coverage
   :file: coverage_table.csv
   :widths: 60, 10, 10, 20
   :header-rows: 1

🛠 Usage
--------

Install package

.. code-block:: bash

    pip3 install gen-dbus

Prepare main entry point by downloading ``main.py`` or create your own.

.. code-block:: bash

    wget -O main.py https://raw.githubusercontent.com/vroncevic/gen_dbus/dev/main.py

Running tool for creating D-Bus IPC projects across supported ``--type``, ``--role``, and ``--bus`` options

.. code-block:: bash

    python3 main.py create --name telemetry_c --type posix_c --role both --bus session --output ./demo/posix_c
    python3 main.py create --name telemetry_cxx --type posix_cxx --role both --bus session --output ./demo/posix_cxx
    python3 main.py create --name telemetry_py --type posix_py --role both --bus session --output ./demo/posix_py

📚 Docs
-------

More documentation and info at

* `gen-dbus.readthedocs.io <https://gen-dbus.readthedocs.io>`_
* `www.python.org <https://www.python.org/>`_

👥 Contributing
---------------

`Contributing to gen_dbus <https://github.com/vroncevic/gen_dbus/blob/dev/CONTRIBUTING.md>`_

📄 Copyright and licence
-------------------------

Copyright (C) 2021 - 2026 by `vroncevic.github.io/gen_dbus <https://vroncevic.github.io/gen_dbus>`_

**gen_dbus** is free software; you can redistribute it and/or modify
it under the same terms as Python itself, either Python version 3.x or,
at your option, any later version of Python 3 you may have available.

Lets help and support PSF.
