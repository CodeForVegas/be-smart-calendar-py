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

# CalDAV Server

The request-handling layer on the server side, intended to be run as a server or daemon for client or server-server peer communications.

Storage is implemented separately to enable filesystem or database or other backends.

The CalDAV Server should be run behind or in conjunction with a proper web server (nginx, apache, etc) and server framework (pyramid, flask, etc). The minimal http interface implemented may be sufficient for internal service or microservice use.
