# Copyright 2021 - 2026 Vladimir Roncevic <elektron.ronca@gmail.com>
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

FROM debian:12
RUN apt-get update
RUN DEBIAN_FRONTEND=noninteractive \
    apt-get install -yq --no-install-recommends \
    tree \
    htop \
    wget \
    curl \
    unzip \
    ca-certificates \
    openssl \
    python3 \
    python3-dev \
    python3-venv \
    python3-wheel \
    libyaml-dev \
    build-essential \
    cmake \
    pkg-config \
    libdbus-1-dev \
    dbus

RUN wget https://bootstrap.pypa.io/get-pip.py
RUN python3 get-pip.py --break-system-packages
RUN python3 -m pip install --break-system-packages --upgrade setuptools pip build
RUN rm -f get-pip.py
COPY requirements.txt /
RUN mkdir /gen_dbus/
COPY gen_dbus /gen_dbus/
COPY pyproject.toml /
COPY MANIFEST.in /
COPY setup.py /
COPY README.md /
COPY LICENSE /
RUN mkdir /tests/
COPY tests /tests/
RUN pip3 install --break-system-packages -r requirements.txt
RUN rm -f requirements.txt
RUN python3 -m build --no-isolation --wheel
RUN pip3 install --break-system-packages /dist/gen_dbus-*-py3-none-any.whl
RUN rm -rf /gen_dbus/ /dist/ /tests/
RUN rm -f setup.py README.md pyproject.toml MANIFEST.in LICENSE
