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

from datetime import datetime, timedelta
from dateutil import rrule
from dataclasses import dataclass
from pydantic import BaseModel

class ToDoForeignData(BaseModel):
	id: int
	dtstamp: datetime
	dtstart: datetime
	due: timedelta
	todo_class: str
	completed: bool
	created: datetime
	description: str
	last_mod: datetime
	location: str
	organizer_id: int
	percent: int
	priority: int
	recur_id: int
	seq: int
	status: str
	summary: str
	url: str
	todo_rrule: str #TODO: Correct type for rrule
	attach: list
	attendee: list
	categories: list
	comment: list
	contact: list
	exdate: datetime
	rstatus: list
	related: list
	resources: list
	rdate: list
	x_prop: dict
	iana_prop: dict

@dataclass
class ToDoData:
	pass
class ToDo(object):
	pass

