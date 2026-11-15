#!/bin/bash
#
# @brief   gen_dbus
# @version 1.1.6
# @date    Sun Nov 15 19:20:00 2026
# @company None, free software to use 2026
# @author  Vladimir Roncevic <elektron.ronca@gmail.com>
#

python3 main.py create --name "telemetry_c" --type "posix_c" --role "both" --bus "session" --output "./demo/posix_c"
python3 main.py create --name "telemetry_cxx" --type "posix_cxx" --role "both" --bus "session" --output "./demo/posix_cxx"
python3 main.py create --name "telemetry_py" --type "posix_py" --role "both" --bus "session" --output "./demo/posix_py"

