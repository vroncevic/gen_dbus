#!/bin/bash
#
# @brief   gen_dbus
# @version v1.0.1
# @date    Sat Aug 11 09:58:41 2021
# @company None, free software to use 2021
# @author  Vladimir Roncevic <elektron.ronca@gmail.com>
#

rm -rf new_simple_test/ full_simple/ latest/ empty_simple_test/
python3 -m coverage run -m --source=../gen_dbus unittest discover -s ./ -p '*_test.py' -vvv
python3 -m coverage html
