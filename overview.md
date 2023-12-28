# Overview

D-Bus is an inter-process communication (IPC) mechanism initially designed to
replace the software component communications systems used by the GNOME and KDE
Linux desktop environments.

Due to the large number of processes involved - adding up processes providing
the services and clients accessing them - establishing one-to-one IPC
communications between all of them becomes an inefficient and quite unreliable
approach. Instead, D-Bus provides a software-bus abstraction that gathers all
the communications between a group of processes over a [single shared virtual
channel](bus_model.md).

Processes connected to a bus don't know how it is internally implemented,
but D-Bus specification guarantees that all processes connected to the bus can
communicate with each other through it.

Linux desktop environments take advantage of the D-Bus facilities by
instantiating multiple buses, notably:

* a single system bus, available to all users and processes of the system, that
provides access to system services (i.e. services provided by the operating
system and also by any system daemons)

![daemon dbus](https://raw.githubusercontent.com/vroncevic/gen_dbus/dev/docs/dbus_multiple_processes_and_daemon_process.png)

* a session bus for each user login session, that provides desktop services to
user applications in the same desktop session, and allows the integration of
the desktop session as a whole.

![libdbus](https://raw.githubusercontent.com/vroncevic/gen_dbus/dev/docs/dbus_multiple_processes.png)

D-Bus provides additional or simplifies existing functionality to the
applications, including information-sharing, modularity and privilege
separation.

[back](README.md)