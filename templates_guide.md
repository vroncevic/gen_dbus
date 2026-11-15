# D-Bus Code Generation Templates Guide (`gen_dbus`)

**gen_dbus** provides production-ready, cross-language wire-compatible **D-Bus IPC** project templates across three POSIX ecosystems:

| `--type` | Language & Standard | D-Bus Library | Build / Packaging | Architecture |
| :--- | :--- | :--- | :--- | :--- |
| `posix_c` | **C11** (`-std=c11 -Wall -Wextra -Wpedantic`) | `libdbus-1` (`pkg-config dbus-1`) | CMake 3.16+ & GNU `Makefile` | Modular vtable dispatcher & typed proxy |
| `posix_cxx` | **C++20** (`-std=c++20 -Wall -Wextra -Wpedantic`) | `libdbus-1` (`pkg-config dbus-1`) | CMake 3.16+ & GNU `Makefile` | Modern RAII (`DBusErrorGuard`, `UniqueConnection`, `UniqueMessage`) |
| `posix_py` | **Python 3.12+** | `dbus-fast` (`asyncio`) | `pyproject.toml` & `requirements.txt` | Clean Architecture, SOLID, `@runtime_checkable Protocol` |

---

## 1. Unified D-Bus Object Model (Cross-Language Interoperable)

All three templates implement the **exact same D-Bus wire contract**, enabling seamless cross-language IPC (for example, a C11 client communicating with a Python `asyncio` server or a C++20 RAII client communicating with a C11 server):

* **Well-Known Bus Name**: `org.vroncevic.<project>.Service`
* **Object Path**: `/org/vroncevic/<project>/Object`
* **Introspection File**: `introspection/org.vroncevic.<project>.xml`
* **Standard D-Bus Interfaces**:
  * `org.freedesktop.DBus.Introspectable` — `Introspect() -> (s xml_data)`
  * `org.freedesktop.DBus.Peer` — `Ping()`, `GetMachineId() -> (s machine_uuid)`
  * `org.freedesktop.DBus.Properties` — `Get(ss) -> (v)`, `Set(ssv)`, `GetAll(s) -> (a{sv})`, and signal `PropertiesChanged(sa{sv}as)`
* **Domain Control Interface** (`org.vroncevic.<project>.Control`):
  * **Method** `Ping(s message) -> (s reply)` — Increments `CallCount`, emits `PropertiesChanged`, and returns formatted pong response.
  * **Method** `SetStatus(s new_status) -> (b applied)` — Updates `Status`, increments `CallCount`, emits `StatusChanged(old_status, new_status)` and `PropertiesChanged`.
  * **Property** `Status` (`s`, `readwrite`) — Readable and writable via `org.freedesktop.DBus.Properties`.
  * **Property** `CallCount` (`u`, `read`) — Read-only operation counter (`uint32`).
  * **Signal** `StatusChanged(s old_status, s new_status)` — Broadcast whenever `Status` transitions.

---

## 2. CLI Options (`create` Subcommand)

```bash
python3 main.py create \
    --name telemetry_svc \
    --type posix_cxx \
    --role both \
    --bus session \
    --output ./telemetry_svc
```

* `--name`: Project / service identifier (required). Hyphens are normalized to underscores for C/C++/Python identifiers and D-Bus object paths.
* `--type`: Target implementation stack (`posix_c`, `posix_cxx`, `posix_py`).
* `--role`: Endpoint generation scope (default `both`):
  * `both`: Generates `dbus_server/`, `dbus_client/`, `introspection/`, and root build files.
  * `client`: Excludes `dbus_server/` and builds/runs only the D-Bus client proxy.
  * `server`: Excludes `dbus_client/` and builds/runs only the D-Bus service daemon.
* `--bus`: Target D-Bus message bus (default `session`):
  * `session`: Binds to `DBUS_BUS_SESSION` / `BusType.SESSION` (ideal for user services and `dbus-run-session` testing).
  * `system`: Binds to `DBUS_BUS_SYSTEM` / `BusType.SYSTEM` (for privileged system daemons with `/etc/dbus-1/system.d/` policies).
* `--output`: Target directory where files are rendered (default `./`).

---

## 3. Building & Running Generated Projects

### 3.1 C11 (`posix_c`) and C++20 (`posix_cxx`)

Install system prerequisites on Debian/Ubuntu:

```bash
sudo apt-get install -y build-essential cmake pkg-config libdbus-1-dev dbus
```

Generate, compile with `make`, and run an isolated ephemeral D-Bus session test:

```bash
python3 main.py create --name sensor_hub --type posix_cxx --role both --bus session --output ./sensor_hub
make -C ./sensor_hub

dbus-run-session -- bash -c '
  ./sensor_hub/build/dbus_server/sensor_hub_server --once &
  sleep 0.3
  ./sensor_hub/build/dbus_client/sensor_hub_client
'
```

### 3.2 Python 3.12+ (`posix_py`)

Install Python dependency:

```bash
pip install dbus-fast>=2.24.0
```

Generate and run inside `dbus-run-session`:

```bash
python3 main.py create --name sensor_hub --type posix_py --role both --bus session --output ./sensor_hub_py
cd ./sensor_hub_py

dbus-run-session -- bash -c '
  python3 -m dbus_server.main --once &
  sleep 0.4
  python3 -m dbus_client.main
'
```

