#!/usr/bin/env python

# Copyright (C) 2015-2016 xtr4nge [_AT_] gmail.com
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.
#

import os

try:
    from mitmproxy import controller, proxy # mitmproxy 0.17
    from mitmproxy.proxy.server import ProxyServer # mitmproxy 0.17
except:
    from libmproxy import controller, proxy # mitmproxy 0.15
    from libmproxy.proxy.server import ProxyServer # mitmproxy 0.15

import logging
from configobj import ConfigObj
from plugins.plugin import Plugin

logger = logging.getLogger("fruityproxy")

class NoCache(Plugin):
    name = "NoCache"
    version = "1.1"

    def response(self, flow):
        
        '''
        flow.response.headers["Cache-Control"] = ["no-store"] # mitmproxy 0.15 [remove]
        flow.response.headers["Pragma"] = ["no-cache"] # mitmproxy 0.15 [remove]
        flow.response.headers["Expires"] = ["Expires","01 Jan 2000 00:00:00 GMT"] # mitmproxy 0.15 [remove]
        '''
        
        flow.response.headers["Cache-Control"] = "no-store"
        flow.response.headers["Pragma"] = "no-cache"
        flow.response.headers["Expires"] = "Sat, 01 Jan 2000 00:00:00 GMT"
        
        logger.debug("["+self.name+"] " + flow.request.host)
        