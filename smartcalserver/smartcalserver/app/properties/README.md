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

# iCalendar Properties

The iCalendar standards spelled out in various RFCs (which cascade to apply fixes and changes) include various Components, and then Properties for the different Components.

For examples:

```sh
BEGIN:VCALENDAR // is the beginning of a Component
NAME;LANG=en:Example Calendar // is the NAME Property with a LANG parameter “en” and a property value of “Example Calendar”
END:VCALENDAR // is the end of a Component
```

Parameter elements have defined iCalendar types per the RFCs and will be encapsulated within the Property classes. In the case of this Python implementation, the iCalendar types will map to Python types with the Property classes are initialized.

## Parsing Incoming Properties

The complexities of the iCalendar Stream are its many RFCs and changes and room for implementation deviations, and in the numer of Property definitions in the various RFCs.

Our defensive parsing scheme will treat incoming Foreign Data as potentially-erroneous and will attempt to validate the incoming data Properties and Parameters according to the specifications (the relevant RFCs) and to common use, though not necessarily in that order.

It will be important to adapt the validation process to real-world scenarios to make a working iCalendar stream parser for the same of the Calendar Server, but there is a fine line between broken and passable error.

Properties defined herein are intended to be general for incoming Properties and Parameters, with additional validation per implenmentation within a Component class (especially within a Pydantic class, which is intended to be more pedantic about the incoming data).

However, it is also important to accept erroneous data wherever possible and store and transmit it as-was-received per the various iCalendar RFCs. The idea is to be as tolerant as possible of the various interpretations of the standards without imposing any fixes or corrections up to the point where the iCalendar stream is functional, if not quite within spec.

## Storing and Manipulating Properties

The use of python dataclasses to manage data structures post-parsing (that is, data that has already been validated or otherwise dealt with from the outside, now stored, managed, and manipulated with internal objects and persistence and whatnot) will make handling of opaque data easier, but must be done with care. Unexpected parameter or property values must still be managed and passed to serialized iCalendar Streams or any client that expects iCalendar streams to move around un-altered (remember, this means keeping unexpected elements from an incoming foreign data stream when re-transmitted, this does **Not** mean to traffic in unexpected elements in object data we create and manipulate locally).

## Internal versus iCalendar Types

The iCalendar RFCs are quite specific about various property and parameter types. These are intended to be serialized to and deserialized from and are not machine representations in many cases (most cases?)

The easiest example is the DATE-TIME type (which applies to many properties) which is a serial string representation similar to this:

```sh
19980119T070000
```

This can be parsed into a python datetime value parsed with datetime.strptime()

```python
>>> datetime.datetime.strptime("19980119T070000", "%Y%m%dT%H%M%S")
datetime.datetime(1998, 1, 19, 7, 0)
```

We can then serialize the internal python datetime representation back to the iCalendar DATE-TIME type:

```python
>>> datetime.datetime(1998, 1, 19, 7, 0).strftime("%Y%m%dT%H%M%S")
'19980119T070000'
```

Thus incoming iCalendar types are parsed and marshalled as needed, to internal types (python types are reasonable for persistence and serialization, if we venture into polyglot data-sharing of internal structures we want to make sure we aren't introducing data errors with unexpected type coercion, etc).

## External References

[ISO 8601](https://en.wikipedia.org/wiki/ISO_8601)
[RFC 3339](https://www.rfc-editor.org/rfc/rfc3339)
[Compare ISO 8601 and RFC 3339](https://ijmacd.github.io/rfc3339-iso8601/)
