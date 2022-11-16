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

# Smart Calendar Server Introduction

There are several CalDAV server projects and of course many commercial implementations of CalDAV servers and clients which we use and encounter daily (Google Calendar and Microsoft Outlook, you have heard of at least of those), why write a Calendar Server and what makes it a Smart Calendar Server?

## Motivation

Using modern methods to parse and manage data and deploy servers as components of larger projects without assuming a monolithic implementation is one reason to pursue this development. The pedagogical value is another, so that a visible and hands-on implementation as part of larger and continued development efforts across the Smart Social and other projects (or even the Smart Calendar Server used on its own) has actual value.

Not to mention, open source projects are a great way to enable communities to see how things work and to build trust in that functionality. Transparency is a good thing quite often, and there is nothing proprietary about how CalDAV and iCalendar and other pieces work. The magic will come from how people in our communities at large use these tools!

## Audience

- A Developer must be able to use and build python-based modules and services, with instructions to do so found with the project source code.
- An Administrator of the server itself should be able to install software in a running cloud environment, or similar. Separate INSTALLATION documentation is found with the source code.
- A general User will likely interact most often through a typical calendar interface found on most mobile devices, on most laptop and desktop computers, and as websites. Embedding of calendars, sharing of icalendar-structured data, sharing of other modern data structures (JSON, GraphQL, etc) and creation of human-readable event content at the SmartCalendar-Server are all on the table, and more.

## Features

This is a quick rundown, more details to be found in other documents here and in the larger-scope Smart Social overview docs, but some ideas to ponder:

- iCalendar and iCalendar Stream export for client use (Google, Apple Calendar apps, etc)
  - Should support RSVP propagation, enable user to add one event to their own calendar(s) and/or subscribe to entire calendar(s)
  - RSVP, Cancel, Update, and other calendar functionality propagated from origin through aggregator
- CalDAV support for calendar API access
  - possibly peer sync
  - update hosted calendar events remotely
- CardDAV support for calendar owners, organizers, possibly participants?
  - Enable some form of public RSVP and contact sharing?
  - Enable basic contacts lookup and network?
- Run as web service through external web server
- Run as daemon for other service interactions
- Expose as library for use in other projects
