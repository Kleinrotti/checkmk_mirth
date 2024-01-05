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
# <name>|<id>|<state>|<channelState>|<sent>|<received>|<filtered>|<error>|<queued>
# <<<mirth_channel:sep(124)>>>
# Test2_channel|5814cb85-d08d-42c4-ac70-80b7cec3eefe|STARTED|Idle|1|1|0|0|0

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
    register,
    Metric
)


@dataclass(frozen=True)
class Channel():
    name: str
    id: str
    state: str
    channelState: str
    sent: str
    received: str
    filtered: int
    error: str
    queued: str


mirth_channel_factory_settings = {
    'mirth_channel_states': {
        'started': 0,
        'stopped': 2,
        'stopping': 2,
        'paused': 1,
        'undeployed': 1,
        'deploying': 1,
        'pausing': 1,
        'starting': 1,
        'syncing': 0,
        'undeploying': 1,
        'unknown': 2,
    },
    'mirth_channel_statistics': {
        'mirth_channel_error': [10, 20],
        'mirth_channel_queued': [40, 70]
    }
}


Section = List[Channel]


def mirth_channel(string_table: StringTable) -> Section:
    return [
        Channel(name, id, state, channelState, int(received),
                int(filtered), int(sent), int(error), int(queued)) for name, id, state, channelState, received,
        filtered, sent, error, queued in string_table
    ]


def discovery_mirth_channel(section: Section) -> DiscoveryResult:
    for item in section:
        yield Service(item=item.name)


def check_mirth_channel(item, params, section: Section) -> CheckResult:
    channel = None
    for sec in section:
        if item == sec.name:
            channel = sec
            break
    if channel is None:
        return None

    levels_queued = params['mirth_channel_statistics']['mirth_channel_queued']
    levels_error = params['mirth_channel_statistics']['mirth_channel_error']

    yield Metric(name = "mirth_channel_sent", value = channel.sent)
    yield Metric(name = "mirth_channel_received", value = channel.received)
    yield Metric(name = "mirth_channel_filtered", value = channel.filtered)
    yield Metric(
        name = "mirth_channel_queued",
        value = channel.queued,
        levels = (levels_queued[0], levels_queued[1]),
    )
    yield Metric(
        name = "mirth_channel_error",
        value = channel.error,
        levels = (levels_error[0], levels_error[1]),
    )
    states = []
    states.append(State(params['mirth_channel_states'][channel.state.lower()]))
    if channel.state.lower() == "undeployed":
        text = "Channel is not deployed"
    else:
        text = f"Channel status: {channel.state}, Connection status: {channel.channelState}"

    if channel.queued >= levels_queued[0]:
        states.append(State.WARN)
    if channel.queued >= levels_queued[1]:
        states.append(State.CRIT)
    if channel.error >= levels_error[0]:
        states.append(State.WARN)
    if channel.error >= levels_error[1]:
        states.append(State.CRIT)

    detail = f"Packets errored: {channel.error}, Packets queued: {channel.queued}"
    # sort the list to get the highest monitoring state easily
    states.sort()

    yield Result(state=states[-1], summary=text, details=detail)


register.agent_section(
    name="mirth_channel",
    parse_function=mirth_channel
)


register.check_plugin(
    name="mirth_channel",
    service_name="Mirth Channel %s",
    sections=['mirth_channel'],
    discovery_function=discovery_mirth_channel,
    check_function=check_mirth_channel,
    check_ruleset_name="mirth_channel",
    check_default_parameters=mirth_channel_factory_settings,
)
