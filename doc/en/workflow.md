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

# Smart Calendar Workflow

The calendar server is intended to be deployed at one more more nodes to act as sharing hubs for various calendars. Perhaps an NNTP analogy could be made, to enable multiple nodes to sync as peers to spread social/public calendars across multiple locations. At the same time, multiple clients can sync from one or more nodes. This enables one user, for example, to sync their own calendar with 1 or more nodes that are aggregating event calendar of interest, even if the nodes are not actively synchronizing as peers.

Using icalendar standards (see References below), any ical-compatible calendar should be shareable to a server so that aggregate calendars may be viewed and manipulated, and published as aggregate icalendar streams (ics).

The CalDAV (and CardDAV if available) standards will be used to communicate where they are in use (most places). The payload is usually an iCalendar stream or an XML document

In addition to aggregating shared calendars, a spider to scan and parse schema.org event markup in indicated content will allow any event pages on websites to be aggregated in similar fashion.

In all cases, the overaching goals are to enable:

- A source of truth for a particular calendar
  - May be a single authoritative source of truth at the origin
  - May be a synchronized peer of the origin for multiple authoritative sources
- Update, RSVP, cancel, and other actions at the origin, propagating through the peer sources in aggregate
- Flexible content publishing (origin content is source of truth, with any additional profile/map visualization/translations etc at the aggregate node)

## External References

[iCalendar Website](https://icalendar.org)

[Google CalDAV v2 Guide](https://developers.google.com/calendar/caldav/v2/guide)
