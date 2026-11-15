#!/bin/bash
#
# @brief   gen_dbus
# @version 1.1.6
# @date    Sun Nov 15 19:20:00 2026
# @company None, free software to use 2026
# @author  Vladimir Roncevic <elektron.ronca@gmail.com>
#

python3 coverage/ats_coverage.py gen_dbus
pylint gen_dbus > gen_dbus.report
echo "Done"

