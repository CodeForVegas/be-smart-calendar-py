# Copyright (C) 2022 Innovate for Vegas Foundation
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

class JournalForeignData(BaseModel):
	uid: str
	dtstamp: datetime.datetime

	vclass: str | None
	created: datetime.datetime | None
	dtstart: datetime.datetime | None
	last_mod: datetime.datetime | None
	organizer: str | None
	recurid: str | None
	seq: int | None
	status: str | None
	summary: str | None
	url: str | None
	rrule: str | None

	attach: str | list[str] | None
	attendee: str | list[str] | None
	categories: str | list[str] | None
	comment: str | list[str] | None
	contact: str | list[str] | None
	description: str | list[str] | None
	exdate: datetime.datetime | list[datetime.datetime] | None
	related: str | list[str] | None
	rdate: datetime.datetime | list[datetime.datetime] | None
	rstatus: str | list[str] | None
	x_prop: str | list[str] | None
	iana_prop: str | list[str] | None

@dataclass
class JournalData:
	pass

class Journal(object):
	pass
