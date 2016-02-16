import cherrypy

class Root(object):
    @cherrypy.expose
    def index(self):
        return "Jan is een gekke boy";
