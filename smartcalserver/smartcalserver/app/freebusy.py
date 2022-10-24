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

from dataclasses import dataclass
from pydantic import BaseModel

import datetime

class FreeBusyForeignData(BaseModel):
	uid: str
	dtstamp: datetime.datetime
	contact: str | None
	dtstart: datetime.datetime | None
	dtend: datetime.datetime | None
	organizer: str | None
	url: str | None

	attendee: str | list[str] | None
	comment: str | list[str] | None
	freebusy: str | list[str] | None
	rstatus: str | list[str] | None
	x_prop: str | list[str] | None
	iana_prop: str | list[str] | None

@dataclass
class FreeBusyData:
	pass

class FreeBusy(object):
	pass
