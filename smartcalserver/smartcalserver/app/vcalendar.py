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


class CalendarForeignData(BaseModel):

	relcalid: str = None
	prodid: str = " PRODID:-//Innovate for Vegas Foundation//NONSGML Smart Calendar//EN"
	version: str
	calscale: str | None
	method: str | None
	x_prop: str | list[str] | None
	iana_prop: str | list[str] | None
	calname: str = None
	caldesc: str = None
	published_ttl: int = 3600


@dataclass
class CalendarData:
	pass

class Calendar(object):
	pass
