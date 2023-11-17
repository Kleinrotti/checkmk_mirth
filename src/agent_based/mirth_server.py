#!/usr/bin/env python3
# -*- encoding: utf-8; py-indent-offset: 4 -*-

# (c) Kleinrotti <kleinrotti@saltcloud.de>

# This is free software;  you can redistribute it and/or modify it
# under the  terms of the  GNU General Public License  as published by
# the Free Software Foundation in version 2.  check_mk is  distributed
# in the hope that it will be useful, but WITHOUT ANY WARRANTY;  with-
# out even the implied warranty of  MERCHANTABILITY  or  FITNESS FOR A
# PARTICULAR PURPOSE. See the  GNU General Public License for more de-
# ails.  You should have  received  a copy of the  GNU  General Public
# License along with GNU Make; see the file  COPYING.  If  not,  write
# to the Free Software Foundation, Inc., 51 Franklin St,  Fifth Floor,
# Boston, MA 02110-1301 USA.

# Sample agent output
# <id>|<activated>|<online>|<expirationDate>|<version>
# <<<mirth_server:sep(124)>>>
# 0bef6dc3-11c1-4a38-80a9-9570cbaf2529|False|False|-|4.4.0

from dataclasses import dataclass
from typing import List

from .agent_based_api.v1.type_defs import (
    CheckResult,
    DiscoveryResult,
    StringTable
)

from .agent_based_api.v1 import (
    Result,
    State,
    Service,
    register
)


@dataclass(frozen=True)
class Server():
    id: str
    activated: str
    online: str
    expirationDate: str
    version: str


mirth_server_factory_settings = {}


Section = List[Server]


def mirth_server(string_table: StringTable) -> Section:
    return [
        Server(id, activated, online, expirationDate, version) for
        id, activated, online, expirationDate, version in string_table
    ]


def discovery_mirth_server(section: Section) -> DiscoveryResult:
    for item in section:
        yield Service(item=item.id)


def check_mirth_server(item, section: Section) -> CheckResult:
    mirth = None
    for sec in section:
        if item == sec.id:
            mirth = sec
            break
    if mirth is None:
        return None
    state = State.OK
    text = f"Version: {mirth.version}"
    detail = (f"License activated: {mirth.activated}\nExpiration: "
              f"{mirth.expirationDate}\nOnline: {mirth.online}")
    yield Result(state=state, summary=text, details=detail)


register.agent_section(
    name="mirth_server",
    parse_function=mirth_server
)


register.check_plugin(
    name="mirth_server",
    service_name="Mirth Server %s",
    sections=['mirth_server'],
    discovery_function=discovery_mirth_server,
    check_function=check_mirth_server
)
