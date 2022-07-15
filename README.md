# Smart Calendar Server Project

A city-scaled calendar-sharing scheme to enable

* Discovery
* Learning
* Participation

using open standards with tools intended to be installed at multiple nodes for flexible and broad utility.

## Project Policies

Unless otherwise and specifically indicated with replacement files in this repository, this project will adhere to the default Code for Vegas Foundation policies for Code of Conduct and Contributing, found at

* [Code of Conduct - Code for Vegas Foundation](https://github.com/CodeForVegas/.github/blob/main/CODE_OF_CONDUCT.md)
* [Contributing to this Project - Code for Vegas Foundation](https://github.com/CodeForVegas/.github/blob/main/CONTRIBUTING.md)

## Workflow

The calendar server is intended to be deployed at one more more nodes to act as sharing hubs for various calendars. Perhaps an NNTP analogy could be made, to enable multiple nodes to sync as peers to spread social/public calendars across multiple locations. At the same time, multiple clients can sync from one or more nodes. This enables one user, for example, to sync their own calendar with 1 or more nodes that are aggregating event calendar of interest, even if the nodes are not actively synchronizing as peers.

Using icalendar standards (see References below), any ical-compatible calendar should be sharable to a server so that aggregate calendars may be viewed and manipulated, and published as aggregate icalendar streams (ics).

CalDAV and CardDAV standards will be used to communicate as well.

In addition to aggregating shared calendars, a spider to scan and parse schema.org event markup in indicated content will allow any event pages on websites to be aggregated in similar fashion.

In all cases, the overarchiving goals are to enable

* A single source of truth for a particular calendar
* Update, RSVP, cancel, and other actions at the origin, propegating through the aggregates
* Flexible content publishing (origin content is source of truth, with any additional profile/map visualization/translations etc at the aggregate node)

## Platform and Tools Selection

The Calendar Server project, owned by Apple Computer and pubilshed under a liberal open source license (see Reference below), is one starting point for the SmartCalender-Server, thus python is also a starting language and, with a sufficiently large set of options for working with vcalendar and other related data and protocols already available.

The Calendar Server project made use of the Twisted asynchronous web framework to handle requests. It will be possible to use Twisted, or Tornado, or perhaps AWS Lamda functions or other to handle large traffic bursts, to be expected during calendar syncs across multiple endpoints. Apple is no longer supporting the Calendar Server project, it has been archived, and is long out of date concerning python versions, etc, so useful for ideas, perhaps, and documentation references. Linked in References section below.

As well there is a more current project, Radicale (see References below) which offers some interesting ideas, also written in python.

Both of these projects are interesting, but should only be taken as inspiration to start the SmartCalendar-Server effort. As well, Radicale may be useful for testing server peering and feature parity checks.

The latest available version of Python that may be used in these scenarios (3.9+) without support for any previous or legacy (2.7 or older) python versions.

Ideally the core services will be deployable as a Serverless Lambda (or other) function, behind an async server, behind something like Django, or perhaps exposed as a server callable behind a Node or GoLang web server. It is possible that the architecture of this implementation will be a candidate for refactoring into another language entirely.

There is a javascript representation of iCalendar data structures out there, it could be on The List to support, especially if Smart Calendar begins down a path of extension.

## Audiences

* A Developer must be able to use and build python-based modules and services, with instructions to do so found with the project source code.
* An Administrator of the server itself should be able to install software in a running cloud environment, or similar. Separate INSTALLATION documentation is found with the source code.
* A general User will likely interact most often through a typical calendar interface found on most mobile devices, on most laptop and desktop computers, and as websites. Embedding of calendars, sharing of icalendar-structured data, and creation of human-readable event content at the SmartCalendar-Server are all on the table, and more.

## Features

* iCalendar and iCalendar Stream export for client use (Google, Apple Calendar apps, etc)
  * Should support RSVP propegation, enable user to add one event to their own calendar(s) and/or subscribe to entire calendar(s)
  * RSVP, Cancel, Update, and other calendar functionality propegated from origin through aggregator
* CalDAV support for calendar API access
  * possibly peer sync
  * update hosted calendar events remotely
* CardDAV support for calendar owners, organizers, possibly participants?
  * Enable some form of public RSVP and contact sharing?
  * Enable basic contacts lookup and network?
* Run as web service through external web server
* Run as daemon for other service interactions
* Expose as library

## References

<https://www.ietf.org/rfc/rfc5545.txt>

<https://www.rfc-editor.org/rfc/rfc8984.html>

<https://icalendar.org>

<http://www.calendarserver.org/>

<https://radicale.org/v3.html>

<https://developers.google.com/calendar/caldav/v2/guide>

<https://github.com/apple/ccs-calendarserver>

<https://devguide.calconnect.org/>
