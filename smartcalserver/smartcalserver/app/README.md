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

# Smart Calendar Application

This is the actual implementation of the Smart Calendar server-side functionality, also appropriately called the Business Logic or maybe the Controller if you like.

The app component of this project *may* move out to its own project repository as a stand-alone code block that could be used in a microservice deployment or something along those lines.

## Architecture Notes

The hierarchy of classes (which at first appear to be quite coupled, and rightfully so) which encapsulate the structure of CalDAV/iCalendar payloads, ics files to email or download, and so on, are coupled because the various specifications of these formats are fairly coupled. While they are extensible, they are specifically extensible, so the parts that are specified are what they are, and so the class hierarchy is designed with that in mind.

<!-- TODO: Should the icalendar components be placed in a module/directory hierarchy ala components/properties/parameters ? -->

### ForeignData Classes

The overhead of pydantic will be applied to incoming foreign data from remote servers or clients submitting items directly to a Smart Calendar.

In the case of server-to-server sharing, the CalDAV protocol and use of iCalendar containers for VCALENDAR objects all assumes that data will be well-formed, but we trust no one. This may cause headaches accounting for all of the deviations and variations between various calendar platforms, but we are doing some defensive programming here.

If there is client data submission to the smart calendar server, the protocol may be RESTful, or other, so we definitely want to leverage pydantic to be pedantic. In cases like this, the specific data may not be CalDAV-compliant, but the data must be well-formed, so the pydantic classes for foreign data would still be useful, if needing to be extended or more created (both seem likely).

Pydantic classes will be used to build internal dataclass models of Smart Calendar objects, which will likely include internal meta data and other extensions, which may or may not be exported to outside clients but which may be useful for internal and local applications and services.

### Dataclass Classes

Handling of data internally occurs through python dataclass objects, which saves some boilerplate trouble and gives us some nice side effects with this standard python3.7+ feature. If we need to deploy an internal-only version of the calendar app module we could strip out the foreigndata interfaces and move the defensive coding with parsing and checking to an outer layer.

There **may** be some utility found in using the attrs library instead of dataclasses, but we began with dataclasses for internal objects committed to data stores and passed around for internal processing.

Whatever the actual implementation, the internal objects should be named and structured as pydantic class analogs, so that the conversion of the foreign data to the internal data objects is fairly obvious. The internal dataclass may have other fields for the sake of internal implementation data (hinted at above) but the relationships for the sake of transformation should be obvious and easily seen.

## References

<https://pydantic-docs.helpmanual.io/>

<https://docs.python.org/3/library/dataclasses.html>

<https://www.attrs.org/en/stable/>
