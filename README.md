<img align="right" src="https://raw.githubusercontent.com/vroncevic/gen_dbus/dev/docs/gen_dbus_logo.png" width="25%">

# Generate DBus

**gen_dbus** is tool for generation of [dbus](overview.md) modules.

Developed in **[python](https://www.python.org/)** code: **100%**.

The README is used to introduce the modules and provide instructions on
how to install the modules, any machine dependencies it may have and any
other information that should be provided before the modules are installed.

[![Python package gen_dbus](https://github.com/vroncevic/gen_dbus/actions/workflows/gen_dbus_package.yml/badge.svg)](https://github.com/vroncevic/gen_dbus/actions/workflows/gen_dbus_package.yml) [![GitHub issues open](https://img.shields.io/github/issues/vroncevic/gen_dbus.svg)](https://github.com/vroncevic/gen_dbus/issues) [![GitHub contributors](https://img.shields.io/github/contributors/vroncevic/gen_dbus.svg)](https://github.com/vroncevic/gen_dbus/graphs/contributors)

<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->
**Table of Contents**

- [Installation](#installation)
    - [Install using pip](#install-using-pip)
    - [Install using setuptools](#install-using-setuptools)
    - [Install using docker](#install-using-docker)
- [Dependencies](#dependencies)
- [Generation flow of py module](#generation-flow-of-py-module)
- [Tool structure](#tool-structure)
- [Docs](#docs)
- [Copyright and Licence](#copyright-and-licence)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->

### Installation

[![Install Python2 Package gen_dbus](https://github.com/vroncevic/gen_dbus/actions/workflows/gen_dbus_python2_publish.yml/badge.svg)](https://github.com/vroncevic/gen_dbus/actions/workflows/gen_dbus_python2_publish.yml) [![Install Python3 Package gen_dbus](https://github.com/vroncevic/gen_dbus/actions/workflows/gen_dbus_python3_publish.yml/badge.svg)](https://github.com/vroncevic/gen_dbus/actions/workflows/gen_dbus_python3_publish.yml)

Currently there are three ways to install tool:
* Install process based on pip
* Install process based on setup.py (setuptools)
* Install process based on docker mechanism

##### Install using pip

Python package is located at **[pypi.org](https://pypi.org/project/gen-dbus/)**.

You can install by using pip
```
# python2
pip install gen-dbus
# python3
pip3 install gen-dbus
```

##### Install using setuptools

Navigate to release **[page](https://github.com/vroncevic/gen_dbus/releases/)** download and extract release archive.

To install modules, locate and run setup.py with arguments
```
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

You can use docker to create image/container.

[![gen_dbus docker checker](https://github.com/vroncevic/gen_dbus/actions/workflows/gen_dbus_docker_checker.yml/badge.svg)](https://github.com/vroncevic/gen_dbus/actions/workflows/gen_dbus_docker_checker.yml)

### Dependencies

**gen_dbus** requires next modules and libraries:

* [ats-utilities - Python App/Tool/Script Utilities](https://vroncevic.github.io/ats_utilities)

### Generation flow of py module

Base flow of generation process:

![alt tag](https://raw.githubusercontent.com/vroncevic/gen_dbus/dev/docs/gen_dbus_flow.png)

### Tool structure

**gen_dbus** is based on OOP:

Generator structure:

```

```

### Docs

[![Documentation Status](https://readthedocs.org/projects/gen_dbus/badge/?version=latest)](https://gen_dbus.readthedocs.io/projects/gen_dbus/en/latest/?badge=latest)

More documentation and info at:
* [gen_dbus.readthedocs.io](https://gen_dbus.readthedocs.io/en/latest/)
* [www.python.org](https://www.python.org/)

### Copyright and Licence

[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0) [![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)

Copyright (C) 2021 by [vroncevic.github.io/gen_dbus](https://vroncevic.github.io/gen_dbus)

**gen_dbus** is free software; you can redistribute it and/or modify
it under the same terms as Python itself, either Python version 2.x/3.x or,
at your option, any later version of Python 3 you may have available.

Lets help and support PSF.

[![Python Software Foundation](https://raw.githubusercontent.com/vroncevic/gen_dbus/dev/docs/psf-logo-alpha.png)](https://www.python.org/psf/)

[![Donate](https://www.paypalobjects.com/en_US/i/btn/btn_donateCC_LG.gif)](https://psfmember.org/index.php?q=civicrm/contribute/transact&reset=1&id=2)
