#!/usr/bin/python
# -*- coding: utf-8 -*-

"""
    Copyright 2012-2013 OpenBroadcaster, Inc.

    This file is part of OpenBroadcaster Remote.

    OpenBroadcaster Remote is free software: you can redistribute it and/or modify
    it under the terms of the GNU Affero General Public License as published by
    the Free Software Foundation, either version 3 of the License, or
    (at your option) any later version.

    OpenBroadcaster Remote is distributed in the hope that it will be useful,
    but WITHOUT ANY WARRANTY; without even the implied warranty of
    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
    GNU Affero General Public License for more details.

    You should have received a copy of the GNU Affero General Public License
    along with OpenBroadcaster Remote.  If not, see <http://www.gnu.org/licenses/>.
"""

from __future__ import absolute_import 

from obplayer.alerts.alert import ObAlert, parse_alert_file
from obplayer.alerts.processor import ObAlertProcessor

Processor = None

def init():
    global Processor
    Processor = ObAlertProcessor()

