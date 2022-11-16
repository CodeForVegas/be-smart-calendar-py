<!--
 Copyright (C) 2022 Innovate for Vegas Foundation
 
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

# SmartCal Broker

This is the Smart Calendar broker component of the SmartCalServer.

Where CalDAV is used to interact with other CalDAV servers and clients using that standard, the SmartCal broker will be used to interact with more modern interfaces, such as REST, GraphQL, etc, to generate profile views, geojson or kml outputs, or whatever a client might be seeking (within the limits of a broker API).
