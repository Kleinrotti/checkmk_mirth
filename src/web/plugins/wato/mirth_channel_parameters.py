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

from cmk.gui.i18n import _
from cmk.gui.plugins.wato.utils import (
    CheckParameterRulespecWithoutItem,
    rulespec_registry,
)
from cmk.gui.plugins.wato.utils import RulespecGroupCheckParametersApplications
from cmk.gui.valuespec import Dictionary, MonitoringState, Tuple, Integer


def _parameter_valuespec_mirth_channel():
    return Dictionary(
        elements=[
            ("mirth_channel_states",
                Dictionary(
                    title = "Parameters for Mirth Channel states",
                    elements = [
                        (
                            "started",
                            MonitoringState(
                                title=_("State when channel is started"),
                                default_value=0,
                            )
                        ),
                        (
                            "starting",
                            MonitoringState(
                                title=_("State when channel is starting"),
                                default_value=0,
                            )
                        ),
                        (
                            "paused",
                            MonitoringState(
                                title=_("State when channel is paused"),
                                default_value=1,
                            ),
                        ),
                        (
                            "pausing",
                            MonitoringState(
                                title=_("State when channel is pausing"),
                                default_value=1,
                            )
                        ),
                        (
                            "stopped",
                            MonitoringState(
                                title=_("State when channel is stopped"),
                                default_value=2,
                            ),
                        ),
                        (
                            "stopping",
                            MonitoringState(
                                title=_("State when channel is stopping"),
                                default_value=2,
                            )
                        ),
                        (
                            "deploying",
                            MonitoringState(
                                title=_("State when channel is deploying"),
                                default_value=0,
                            )
                        ),
                        (
                            "undeployed",
                            MonitoringState(
                                title=_("State when a channel is undeployed"),
                                default_value=1,
                            ),
                        ),
                        (
                            "undeploying",
                            MonitoringState(
                                title=_("State when channel is undeploying"),
                                default_value=1,
                            )
                        ),
                        (
                            "unknown",
                            MonitoringState(
                                title=_("State when channel is unknown"),
                                default_value=2,
                            )
                        )
                    ],
                    optional_keys=[]
                )
             ),
            ("mirth_channel_statistics",
                Dictionary(
                    title = "Parameters for Mirth Statistics",
                    elements = [
                        ('mirth_channel_error', Tuple(
                            title = 'Levels for error messages',
                            help = "Number of error messages for warning or critical state",
                            elements = [
                                Integer(title = "Warning at", default_value = 10),
                                Integer(title = "Critical at", default_value = 20),
                            ])),
                        ('mirth_channel_queued', Tuple(
                            title = 'Levels for queued messages',
                            help = "Number of queued messages for warning or critical state",
                            elements = [
                                Integer(title = "Warning at", default_value = 40),
                                Integer(title = "Critical at", default_value = 70),
                            ])),
                    ],
                    optional_keys=[]
                ),
             ),
        ]
    )


rulespec_registry.register(
    (
        CheckParameterRulespecWithoutItem(
            check_group_name="mirth_channel",
            group=RulespecGroupCheckParametersApplications,
            parameter_valuespec=_parameter_valuespec_mirth_channel,
            title=lambda: _("Mirth Channel Parameters")
        )
    )
)
