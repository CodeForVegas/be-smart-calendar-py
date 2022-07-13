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

import logging
from http.server import BaseHTTPRequestHandler


class HandleCalDAVRequest(BaseHTTPRequestHandler):

	def do_HEAD(self):
		logging.debug("do_HEAD")
		pass

	def do_GET(self):
		logging.debug("do_GET")
		# This is a test block early in development, will be converted to real code
		# and this block could be turned into in-band error/status output along the way
		message = '\n'.join([
    		'CLIENT VALUES:',
        	'client_address=%s (%s)' % (self.client_address,
            	self.address_string()),
        	'command=%s' % self.command,
        	'path=%s' % self.path,
        	'request_version=%s' % self.request_version,
        	'',
        	'SERVER VALUES:',
        	'server_version=%s' % self.server_version,
        	'sys_version=%s' % self.sys_version,
        	'protocol_version=%s' % self.protocol_version,
        	'',
        	])

		self.send_response(200)
		self.send_header('content-length', len(message))
		self.send_header('content-type', 'text/plain')
		self.end_headers()
		self.wfile.write(bytes(message, 'UTF-8'))

	def do_PUT(self):
		logging.debug("do_PUT")
		pass

	def do_POST(self):
		logging.debug("do_POST")
		pass

	def do_MKCALENDAR(self):
		logging.debug("do_MKCALENDAR")
		pass

	def do_MKCOL(self):
		logging.debug("do_MKCOL")
		pass

	def do_DELETE(self):
		logging.debug("do_DELETE")
		pass

	def do_OPTIONS(self):
		logging.debug("do_OPTIONS")
		pass

	def do_PROPFIND(self):
		logging.debug("do_PROPFIND")
		pass

	def do_PROPPATCH(self):
		logging.debug("do_PROPPATCH")
		pass

	def do_REPORT(self):
		logging.debug("do_REPORT")
		pass

	def do_AUDIO(self):
		logging.debug("do_AUDIO")
		pass
