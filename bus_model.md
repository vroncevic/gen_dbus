# Bus Model

Every connection to a bus is identified in the context of D-Bus by what is
called a bus name. A bus name consists of two or more dot-separated strings
of letters, digits, dashes, and underscores. An example of a valid bus name
is org.freedesktop.NetworkManager.

When a process sets up a connection to a bus, the bus assigns to the connection
a special bus name called unique connection name. Bus names of this type are
immutable - it's guaranteed they won't change as long as the connection
exists - and, more importantly, they can't be reused during the bus lifetime.
This means that no other connection to that bus will ever have assigned such
unique connection name, even if the same process closes down the connection to
the bus and creates a new one. Unique connection names are easily recognizable
because they start with the—otherwise forbidden—colon character. An example of
a unique connection name is :1.1553 (the characters after the colon have no
particular meaning).

A process can ask for additional bus names for its connection, provided that
any requested name is not already being used by another connection to the bus.
In D-Bus parlance, when a bus name is assigned to a connection, it is said the
connection owns the bus name. In that sense, a bus name can't be owned by two
connections at the same time, but, unlike unique connection names, these names
can be reused if they are available: a process may reclaim a bus name
released - purposely or not - by another process.

The idea behind these additional bus names, commonly called well-known names,
is to provide a way to refer to a service using a prearranged bus name.
For instance, the service that reports the current time and date in the system
bus lies in the process whose connection owns the org.freedesktop.timedate1 bus
name, regardless of which process it is.

Bus names can be used as a simple way to implement single-instance applications
(second instances detect that the bus name is already taken). It can also be
used to track a service process lifecycle, since the bus sends a notification
when a bus name is released due to a process termination.

# Object model

Because of its original conception as a replacement for several component
oriented communications systems, D-Bus shares with its predecessors an object
model in which to express the semantics of the communications between clients
and services. The terms used in the D-Bus object model mimic those used by
some object oriented programming languages. That doesn't mean that D-Bus is
somehow limited to OOP languages —in fact, the most used implementation
(libdbus) is written in C, a procedural programming language.

In D-Bus, a process offers its services by exposing objects. These objects have
methods that can be invoked, and signals that the object can emit.
Methods and signals are collectively referred to as the members of the object.
Any client connected to the bus can interact with an object by using its
methods, making requests or commanding the object to perform actions.
For instance, an object representing a time service can be queried by a client
using a method that returns the current date and time. A client can also listen
to signals that an object emits when its state changes due to certain events,
usually related to the underlying service. An example would be when a service
that manages hardware devices —such as USB or network drivers— signals a
"new hardware device added" event. Clients should instruct the bus that they
are interested in receiving certain signals from a particular object, since a
D-Bus bus only passes signals to those processes with a registered interest in
them.

A process connected to a D-Bus bus can request it to export as many D-Bus
objects as it wants. Each object is identified by an object path, a string of
numbers, letters and underscores separated and prefixed by the slash character,
called that because of their resemblance to Unix filesystem paths.
The object path is selected by the requesting process, and must be unique in
the context of that bus connection. An example of a valid object path is
/org/kde/kspread/sheets/3/cells/4/5. However, it's not enforced —but also
not discouraged— to form hierarchies within object paths.
The particular naming convention for the objects of a service is entirely up
to the developers of such service, but many developers choose to namespace
them using the reserved domain name of the project as a prefix (e.g. /org/kde).

Every object is inextricably associated to the particular bus connection where
it was exported, and, from the D-Bus point of view, only lives in the context
of such connection. Therefore, in order to be able to use a certain service,
a client must indicate not only the object path providing the desired service,
but also the bus name under which the service process is connected to the bus.
This in turn allows that several processes connected to the bus can export
different objects with identical object paths unambiguously.

Members —methods and signals— that can be used with an object are specified by
an interface. An interface is a set of declarations of methods (including its
passing and returning parameters) and signals (including its parameters)
identified by a dot-separated name resembling the Java language interfaces
notation. An example of a valid interface name is org.freedesktop.

Introspectable. Despite their similarity, interface names and bus names should
not be mistaken. A D-Bus object can implement several interfaces, but at least
must implement one, providing support for every method and signal defined by
it. The combination of all interfaces implemented by an object is called the
object type.

When using an object, it's a good practice for the client process to provide
the member's interface name besides the member's name, but is only mandatory
when there is an ambiguity caused by duplicated member names available from
different interfaces implemented by the object —otherwise, the selected member
is undefined or erroneous. An emitted signal, on the other hand, must always
indicate to which interface it belongs.

The D-Bus specification also defines several standard interfaces that objects
may want to implement in addition to its own interfaces. Although technically
optional, most D-Bus service developers choose to support them in their
exported objects since they offer important additional features to D-Bus
clients, such as introspection. These standard interfaces are:

* org.freedesktop.DBus.Peer: test if D-Bus connection is alive.
* org.freedesktop.DBus.Introspectable: provides an introspection mechanism by
which a client process can, at run-time, get a description (in XML format) of
the interfaces, methods and signals that the object implements.
* org.freedesktop.DBus.Properties: allows a D-Bus object to expose the
underlying native object properties or attributes, or simulate them if it
doesn't exist.
* org.freedesktop.DBus.ObjectManager: when a D-Bus service arranges its
objects hierarchically, this interface provides a way to query an object
about all sub-objects under its path, as well as their interfaces and
properties, using a single method call.

The D-Bus specification defines a number of administrative bus operations
(called "bus services") to be performed using the /org/freedesktop/DBus object
that resides in the org.freedesktop.DBus bus name. Each bus reserves this
special bus name for itself, and manages any requests made specifically to
this combination of bus name and object path. The administrative operations
provided by the bus are those defined by the object's interface
org.freedesktop.DBus. These operations are used for example to provide
information about the status of the bus,[5] or to manage the request and
release of additional well-known bus names.

# Communications model
D-Bus was conceived as a generic, high-level inter-process communication
system. To accomplish such goals, D-Bus communications are based on the
exchange of messages between processes instead of "raw bytes". D-Bus messages
are high-level discrete items that a process can send through the bus to
another connected process. Messages have a well-defined structure (even the
types of the data carried in their payload are defined), allowing the bus to
validate them and to reject any ill-formed message. In this regard, D-Bus is
closer to an RPC mechanism than to a classic IPC mechanism, with its own type
definition system and its own marshaling.

The bus supports two modes of interchanging messages between a client and a
service process:

* One-to-one request-response: This is the way for a client to invoke an
object's method. The client sends a message to the service process exporting
the object, and the service in turn replies with a message back to the client
process. The message sent by the client must contain the object path, the name
of the invoked method (and optionally the name of its interface), and the
values of the input parameters (if any) as defined by the object's selected
interface. The reply message carries the result of the request, including the
values of the output parameters returned by the object's method invocation,
or exception information if there was an error.

* Publish/subscribe: This is the way for an object to announce the occurrence
of a signal to the interested parties. The object's service process broadcasts
a message that the bus passes only to the connected clients subscribed to the
object's signal. The message carries the object path, the name of the signal,
the interface to which the signal belongs, and also the values of the signal's
parameters (if any). The communication is one-way: there are no response
messages to the original message from any client process, since the sender
knows neither the identities nor the number of the recipients.
Every D-Bus message consists of a header and a body. The header is formed by
several fields that identify the type of message, the sender, as well as
information required to deliver the message to its recipient (destination bus
name, object path, method or signal name, interface name, etc.). The body
contains the data payload that the receiver process interprets —for instance
the input or output arguments. All the data is encoded in a well known binary
format called the wire format which supports the serialization of various
types, such as integers and floating-point numbers, strings, compound types,
and so on, also referred to as marshaling.

The D-Bus [specification](architecture.md) defines the wire protocol: how to build the D-Bus
messages to be exchanged between processes within a D-Bus connection.
However, it does not define the underlying transport method for delivering
these messages.
