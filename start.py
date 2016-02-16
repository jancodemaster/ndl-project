#!/usr/bin/python

import cherrypy
from controllers import Root

cherrypy.quickstart(Root())
