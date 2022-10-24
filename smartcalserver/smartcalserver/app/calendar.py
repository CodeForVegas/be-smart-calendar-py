# Copyright (C) 2022 Code for Vegas Foundation
# 
# This file is part of be-smart-calendar-server-py.
# 
# be-smart-calendar-server-py is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
# 
# be-smart-calendar-server-py is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
# 
# You should have received a copy of the GNU General Public License
# along with be-smart-calendar-server-py.  If not, see <http://www.gnu.org/licenses/>.

#import vobject
from datetime import datetime
from dataclasses import dataclass
from pydantic import BaseModel

class CalendarForeignData(BaseModel):
	id: int
	guid: str = None
	relcalid: str = None
	prodid: str = " PRODID:-//Code for Vegas Foundation//NONSGML Smart Calendar//EN"
	calname: str = None
	caldesc: str = None
	calscale: str = "GREGORIAN"
	published_ttl: int = 3600


@dataclass
class CalendarData:
	pass

class Calendar(object):
	pass
