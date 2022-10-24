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

from datetime import datetime
from dataclasses import dataclass
from pydantic import BaseModel

class FreeBusyForeignData(BaseModel):
	id: int
	dtstamp: datetime
	dtstart: datetime
	dtend: datetime
	contact: str
	organizer: str
	url: str
	attendee: str
	comment: str
	freebusy: str
	rstatus: str
	x_prop: dict
	iana_prop: dict

@dataclass
class FreeBusyData:
	pass

class FreeBusy(object):
	pass
