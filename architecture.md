# Architecture

Most existing D-Bus implementations follow the architecture of the reference
implementation. This architecture consists of two main components:

* a point-to-point communications library that implements the D-Bus wire
protocol in order to exchange messages between two processes. In the reference
implementation this library is libdbus. In other implementations libdbus may
be wrapped by another higher-level library, language binding, or entirely
replaced by a different standalone implementation that serves the same purpose.
This library only supports one-to-one communications between two processes.

* a special daemon process that plays the bus role and to which the rest of
the processes connect using any D-Bus point-to-point communications library.
This process is also known as the message bus daemon, since it is responsible
for routing messages from any process connected to the bus to another. In the
reference implementation this role is performed by dbus-daemon, which itself
is built on top of libdbus. Another implementation of the message bus daemon
is dbus-broker, which is built on top of sd-bus.

The libdbus library (or its equivalent) internally uses a native lower-level
IPC mechanism to transport the required D-Bus messages between the two
processes in both ends of the D-Bus connection. D-Bus specification doesn't
mandate which particular IPC transport mechanisms should be available to use,
as it's the communications library that decides what transport methods it
supports. For instance, in Unix-like operating systems such as Linux libdbus
typically uses Unix domain sockets as the underlying transport method, but it
also supports TCP sockets.

The communications libraries of both processes must agree on the selected
transport method and also on the particular channel used for their
communication. This information is defined by what D-Bus calls an address.
Unix-domain socket are filesystem objects, and therefore they can be
identified by a filename, so a valid address would be
unix:path=/tmp/.hiddensocket. Both processes must pass the same address to
their respective communications libraries to establish the D-Bus connection
between them. An address can also provide additional data to the communications
library in the form of comma-separated key=value pairs. This way, for example,
it can provide authentication information to a specific type of connection
that supports it.

When a message bus daemon like dbus-daemon is used to implement a D-Bus bus,
all processes that want to connect to the bus must know the bus address, the
address by which a process can establish a D-Bus connection to the central
message bus process. In this scenario, the message bus daemon selects the bus
address and the remainder processes must pass that value to their corresponding
libdbus or equivalent libraries. dbus-daemon defines a different bus address
for every bus instance it provides. These addresses are defined in the daemon's
configuration files.

Two processes can use a D-Bus connection to exchange messages directly between
them, but this is not the way in which D-Bus is normally intended to be used.
The usual way is to always use a message bus daemon (i.e. dbus-daemon) as a
communications central point to which each process should establish its
point-to-point D-Bus connection. When a process —client or service— sends a
D-Bus message, the message bus process receives it in the first instance and
delivers it to the appropriate recipient. The message bus daemon may be seen
as a hub or router in charge of getting each message to its destination by
repeating it through the D-Bus connection to the recipient process.
The recipient process is determined by the destination bus name in the
message's header field, or by the subscription information to signals
maintained by the message bus daemon in the case of signal propagation
messages. The message bus daemon can also produce its own messages as a
response to certain conditions, such as an error message to a process that
sent a message to a nonexistent bus name.

dbus-daemon improves the feature set already provided by D-Bus itself with
additional functionality. For example, service activation allows automatic
starting of services when needed —when the first request to any bus name of
such service arrives at the message bus daemon. This way, service processes
neither need to be launched during the system initialization or user
initialization stage nor need they consume memory or other resources when not
being used. This feature was originally implemented using setuid helpers, but
nowadays it can also be provided by systemd's service activation framework.
Service activation is an important feature that facilitates the management of
the process lifecycle of services (for example when a desktop component should
start or stop).

[back](bus_model.md)