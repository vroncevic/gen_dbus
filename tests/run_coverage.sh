#!/bin/bash
#
# @brief   gen_dbus
# @version v1.0.1
# @date    Sat Aug 11 09:58:41 2021
# @company None, free software to use 2021
# @author  Vladimir Roncevic <elektron.ronca@gmail.com>
#

rm -rf htmlcov gen_dbus_coverage.xml gen_dbus_coverage.json .coverage
rm -rf new_simple_test/ full_simple/ latest/ empty_simple_test/
ats_coverage_run.py -n gen_dbus -p ../README.md
rm -rf new_simple_test/ full_simple/ latest/ empty_simple_test/
python3 -m coverage run -m --source=../gen_dbus unittest discover -s ./ -p '*_test.py' -vvv
python3 -m coverage html -d htmlcov
python3 -m coverage xml -o gen_dbus_coverage.xml 
python3 -m coverage json -o gen_dbus_coverage.json
python3 -m coverage report --format=markdown -m
