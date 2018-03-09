"""
Registry that contains the Workers and Reducer's data, to be contacted from outer actors
"""

from pyactor.context import set_context, create_host, serve_forever

class NotFound(Exception):
    pass

class Registry(object):
    _ask = ['get_all', 'bind', 'lookup', 'unbind']
    _tell = []
    _ref = ['get_all', 'bind', 'lookup']

    def __init__(self):
        self.actors = {}
        self.reducer = {}

    def bind(self, name, actor):
        if name == 'reducer':
            print 'registered reducer'
            self.reducer[name] = actor
        else:
            print "registered", name
            self.actors[name] = actor

    def unbind(self, name):
        if name in self.actors.keys():
            del self.actors[name]
        elif name in self.reducer.keys():
            del self.reducer[name]
        else:
            raise NotFound()

    def lookup(self, name):
        if name == 'reducer':
            return self.reducer['reducer']
        elif name in self.actors:
            return self.actors[name]
        return None

    def get_all(self):
        return self.actors.values()


if __name__ == "__main__":
    set_context()
    host = create_host('http://127.0.0.1:6000/')

    registry = host.spawn('registry', Registry)

    print 'host listening at port 6000'

    serve_forever()
