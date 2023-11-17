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

from cmk.gui.plugins.metrics import metric_info

metric_info["mirth_channel_sent"] = {
    "title": _("Sent"),
    "unit": "count",
    "color": "13/a",
}
metric_info["mirth_channel_received"] = {
    "title": _("Received"),
    "unit": "count",
    "color": "34/a",
}
metric_info["mirth_channel_filtered"] = {
    "title": _("Filtered"),
    "unit": "count",
    "color": "44/a",
}
metric_info["mirth_channel_queued"] = {
    "title": _("Queued"),
    "unit": "count",
    "color": "16/a",
}

metric_info["mirth_channel_error"] = {
    "title": _("Errors"),
    "unit": "count",
    "color": "46/a",
}
