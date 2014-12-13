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

from obplayer.task import ObThread
from obplayer.log import *
from obplayer.data import *
from obplayer.main import ObMainApp
from obplayer.gui import *
from obplayer.player import *

Log = None

Config = None
RemoteData = None
PlaylogData = None

Player = None

Gui = None
Main = None

def main():
    ObMainApp().start()

