"""
Registry that contains the Workers and Reducer's data, to be contacted from outer actors
Authors: Amanda Gomez Gomez, Oussama El Azizi
"""

from pyactor.context import set_context, create_host, serve_forever
import sys


class NotFound(Exception):
    """
    Not found Exception.
    """

    pass


class Registry(object):
    """
    Name service resolver actor.
    """

    _ask = ['get_all', 'bind', 'lookup', 'unbind']
    _tell = []
    _ref = ['get_all', 'bind', 'lookup']

    def __init__(self):
        """
        Constructor
        """

        self.actors = {}
        self.reducer = {}

    def bind(self, name, actor):
        """
        Bind a name to an spawned reference of an actor.
        Reducer and Mappers are binded in different lists.
        :param name: name to be recognized with (unique)
        :param actor: spawned reference
        :return:
        """

        if name == 'reducer':
            print 'registered reducer'
            self.reducer[name] = actor
        else:
            print "registered", name
            self.actors[name] = actor

    def unbind(self, name):
        """
        Delete the binded reference between a name and an actor.
        :param name: name to be deleted
        :return:
        """

        if name in self.actors.keys():
            del self.actors[name]
        elif name in self.reducer.keys():
            del self.reducer[name]
        else:
            raise NotFound()

    def lookup(self, name):
        """
        Function to make query's to the registry.
        :param name: actor identification
        :return: actor spawned reference
        """

        if name == 'reducer':
            return self.reducer['reducer']
        elif name in self.actors:
            return self.actors[name]
        return None

    def get_all(self):
        """
        Obtain all the actors references in the actors map (does not return the reducers).
        :return: actors spawned reference list
        """

        return self.actors.values()


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print "Incorrect call, specify one argument, corresponding to the local IP."
        quit()

    set_context()
    address = 'http://' + sys.argv[1] + ':5999/'
    host = create_host(address)

    registry = host.spawn('registry', Registry)

    print 'host listening at port 5999'

    serve_forever()
