#!/bin/bash
#
# @brief   gen_dbus
# @version 1.1.6
# @date    Sun Nov 15 19:20:00 2026
# @company None, free software to use 2026
# @author  Vladimir Roncevic <elektron.ronca@gmail.com>
#

python3 gates/gates/interfaces_checker.py gen_dbus
python3 gates/gates/isp_checker.py gen_dbus
python3 gates/gates/limits_checker.py gen_dbus
python3 gates/gates/srp_checker.py gen_dbus

echo "Done"
