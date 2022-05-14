<img align="right" src="https://raw.githubusercontent.com/vroncevic/gen_dbus/dev/docs/gen_dbus_logo.png" width="25%">

# Generate DBus

☯️ **gen_dbus** is tool for generation of [dbus](overview.md) modules.

Developed in 🐍 **[python](https://www.python.org/)** code.

The README is used to introduce the modules and provide instructions on
how to install the modules, any machine dependencies it may have and any
other information that should be provided before the modules are installed.

[![gen_dbus python checker](https://img.shields.io/github/workflow/status/vroncevic/gen_dbus/gen_dbus_python_checker?style=flat&label=gen_dbus%20python%20checker)](https://github.com/vroncevic/gen_dbus/actions/workflows/gen_dbus_python_checker.yml) [![gen_dbus package checker](https://img.shields.io/github/workflow/status/vroncevic/gen_dbus/gen_dbus_package_checker?style=flat&label=gen_dbus%20package%20checker)](https://github.com/vroncevic/gen_dbus/actions/workflows/gen_dbus_package_checker.yml) [![GitHub issues open](https://img.shields.io/github/issues/vroncevic/gen_dbus.svg)](https://github.com/vroncevic/gen_dbus/issues) [![GitHub contributors](https://img.shields.io/github/contributors/vroncevic/gen_dbus.svg)](https://github.com/vroncevic/gen_dbus/graphs/contributors)

<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->
**Table of Contents**

- [Installation](#installation)
    - [Install using pip](#install-using-pip)
    - [Install using build](#install-using-build)
    - [Install using py setup](#install-using-py-setup)
    - [Install using docker](#install-using-docker)
- [Dependencies](#dependencies)
- [Generation flow of py module](#generation-flow-of-py-module)
- [Tool structure](#tool-structure)
- [Docs](#docs)
- [Contributing](#contributing)
- [Copyright and Licence](#copyright-and-licence)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->

### Installation

Used next development environment

![Development environment](https://raw.githubusercontent.com/vroncevic/gen_dbus/dev/docs/ubuntuxis.png)

[![gen_dbus python2 build](https://img.shields.io/github/workflow/status/vroncevic/gen_dbus/gen_dbus_python2_build?style=flat&label=gen_dbus%20python2%20build)](https://github.com/vroncevic/gen_dbus/actions/workflows/gen_dbus_python2_build.yml) [![gen_dbus python3 build](https://img.shields.io/github/workflow/status/vroncevic/gen_dbus/gen_dbus_python3_build?style=flat&label=gen_dbus%20python3%20build)](https://github.com/vroncevic/gen_dbus/actions/workflows/gen_dbus_python3_build.yml)

Currently there are three ways to install package
* Install process based on using pip mechanism
* Install process based on build mechanism
* Install process based on setup.py mechanism
* Install process based on docker mechanism

##### Install using pip

Python 📦 is located at **[pypi.org](https://pypi.org/project/gen-dbus/)**.

You can install by using pip

```bash
# python2
pip install gen-dbus
# python3
pip3 install gen-dbus
```

##### Install using build

Navigate to release **[page](https://github.com/vroncevic/gen_dbus/releases/)** download and extract release archive 📦.

To install **gen_dbus** 📦 type the following

```bash
tar xvzf gen_dbus-x.y.z.tar.gz
cd gen_dbus-x.y.z/
# python2
wget https://bootstrap.pypa.io/pip/2.7/get-pip.py
python2 get-pip.py 
python2 -m pip install --upgrade setuptools
python2 -m pip install --upgrade pip
python2 -m pip install --upgrade build
pip2 install -r requirements.txt
python2 -m build --no-isolation --wheel
pip2 install ./dist/gen_dbus-*-py2-none-any.whl
rm -f get-pip.py
chmod 755 /usr/local/lib/python2.7/dist-packages/usr/local/bin/gen_dbus_run.py
ln -s /usr/local/lib/python2.7/dist-packages/usr/local/bin/gen_dbus_run.py /usr/local/bin/gen_dbus_run.py
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
chmod 755 /usr/local/lib/python3.9/dist-packages/usr/local/bin/gen_dbus_run.py
ln -s /usr/local/lib/python3.9/dist-packages/usr/local/bin/gen_dbus_run.py /usr/local/bin/gen_dbus_run.py
```

##### Install using py setup

Navigate to release **[page](https://github.com/vroncevic/gen_dbus/releases/)** download and extract release archive 📦.

To install **gen_dbus** 📦 locate and run setup.py with arguments

```bash
tar xvzf gen_dbus-x.y.z.tar.gz
cd gen_dbus-x.y.z/
# python2
pip install -r requirements.txt
python setup.py install_lib
python setup.py install_data
python setup.py install_egg_info
# python3
pip3 install -r requirements.txt
python3 setup.py install_lib
python3 setup.py install_data
python3 setup.py install_egg_info
```

##### Install using docker

You can use Dockerfile to create image/container 🚢.

[![gen_dbus docker checker](https://img.shields.io/github/workflow/status/vroncevic/gen_dbus/gen_dbus_docker_checker?style=flat&label=gen_dbus%20docker%20checker)](https://github.com/vroncevic/gen_dbus/actions/workflows/gen_dbus_docker_checker.yml)

### Dependencies

**gen_dbus** requires next modules and libraries

* [ats-utilities - Python App/Tool/Script Utilities](https://vroncevic.github.io/gen_dbus)

### Generation flow of py module

Base flow of generation process

![Generation flow](https://raw.githubusercontent.com/vroncevic/gen_dbus/dev/docs/gen_dbus_flow.png)

### Tool structure

**gen_dbus** is based on OOP

🧰 Generator structure

```bash
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

23 directories, 78 files
```

### Docs

[![Documentation Status](https://readthedocs.org/projects/gen_dbus/badge/?version=latest)](https://gen_dbus.readthedocs.io/en/latest/?badge=latest)

📗 More documentation and info at

* [gen_dbus.readthedocs.io](https://gen_dbus.readthedocs.io/en/latest/)
* [www.python.org](https://www.python.org/)

### Contributing

🌎 🌍 🌏 [Contributing to gen_dbus](CONTRIBUTING.md)

### Copyright and Licence

[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0) [![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)

Copyright (C) 2021 by [vroncevic.github.io/gen_dbus](https://vroncevic.github.io/gen_dbus)

**gen_dbus** is free software; you can redistribute it and/or modify
it under the same terms as Python itself, either Python version 2.x/3.x or,
at your option, any later version of Python 3 you may have available.

Lets help and support PSF.

[![Python Software Foundation](https://raw.githubusercontent.com/vroncevic/gen_dbus/dev/docs/psf-logo-alpha.png)](https://www.python.org/psf/)

[![Donate](https://www.paypalobjects.com/en_US/i/btn/btn_donateCC_LG.gif)](https://psfmember.org/index.php?q=civicrm/contribute/transact&reset=1&id=2)
