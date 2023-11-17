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
    HostRulespec,
    rulespec_registry,
)
from cmk.gui.plugins.wato.datasource_programs import RulespecGroupDatasourcePrograms
from cmk.gui.valuespec import Dictionary, TextAscii, Integer, FixedValue, Password
from cmk.gui.watolib.rulespecs import Rulespec


def _factory_default_special_agents_mirth():
    # No default, do not use setting if no rule matches
    return Rulespec.FACTORY_DEFAULT_UNUSED


def _valuespec_special_agents_mirth():
    return Dictionary(
        elements=[
            ("username",
             TextAscii(
                 title=_("Username"),
                 allow_empty=False,
             )
             ),
            ("secret",
             Password(
                 title=_("Secret"),
                 allow_empty=False,
             )
             ),
            ("port",
             Integer(
                 title=_("Port"),
                 default_value=8443,
             )
             ),
            ("log_fetch_size",
             Integer(
                 title="Maximum number of log entries to fetch",
                 default_value=10
             )
             ),
            ("verify_ssl",
             FixedValue(
                 value=True,
                 title=_("Verify SSL certificate"),
                 totext=_("Certificate validation enabled"),
             ),
             ),
            ("log_services",
             FixedValue(
                 title="Disable Mirth log services",
                 value=False,
                 default_value=True,
                 totext=_("Log services are disabled now"),
             )
             )
        ],
        optional_keys=["verify_ssl", "log_services"],
        title=_("Mirth Special Agent Configuration"),
        help=_("This rule enables the Mirth Special Agent "
               "which collects the data through the Mirth REST API."),
    )


rulespec_registry.register(
    (
        HostRulespec(
            factory_default=_factory_default_special_agents_mirth(),
            group=RulespecGroupDatasourcePrograms,
            name="special_agents:mirth",
            valuespec=_valuespec_special_agents_mirth,
        )
    )
)
