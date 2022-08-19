<!--
 Copyright (C) 2022 Code for Vegas Foundation
 
 This file is part of be-smart-calendar-server-py.
 
 be-smart-calendar-server-py is free software: you can redistribute it and/or modify
 it under the terms of the GNU General Public License as published by
 the Free Software Foundation, either version 3 of the License, or
 (at your option) any later version.
 
 be-smart-calendar-server-py is distributed in the hope that it will be useful,
 but WITHOUT ANY WARRANTY; without even the implied warranty of
 MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 GNU General Public License for more details.
 
 You should have received a copy of the GNU General Public License
 along with be-smart-calendar-server-py.  If not, see <http://www.gnu.org/licenses/>.
-->

# Broker parts of CalDAV Server

Deal with incoming and outgoing CalDAV transaction data, passing (brokering) the payloads to and from the app layer (or service, or... ?)

## References

[Python vcalendar and vcard library](http://eventable.github.io/vobject/)

[Radicale Server Implementation (useful broker implementation)](https://github.com/Kozea/Radicale)
