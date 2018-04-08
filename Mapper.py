"""
Workers to be binded to the registry and later used to spawn Mappers.
The call takes 1 parameter, to specify the number of the worker.
Authors: Amanda Gomez Gomez, Oussama El Azizi
"""

import sys

from pyactor.context import set_context, create_host, serve_forever


class Map(object):
    """
    Actor Map.
    """
    _tell = ['map', 'set_http_server']
    _ref = ['map']

    def __init__(self):
        """
        Constructor
        """
        self.http_server = ''

    def map(self, i, reducer, map_func, red_func):
        """
        Calls the map function and sends the mapped data to the reducer.
        :param i: identification number
        :param reducer: reducer instance
        :param map_func: map function
        :param red_func: reduce function
        :return:
        """
        file_name = 'part' + str(i)
        mapped_words = map_func(file_name, self.http_server, reducer)
        print "Mapper finished"
        reducer.reduce(mapped_words, red_func)

    def set_http_server(self, addr):
        """
        Setting the HTTP server URL.
        :param addr: URL without port
        :return:
        """
        self.http_server = addr + ':8000'


if __name__ == "__main__":
    if len(sys.argv) != 4:
        print "Incorrect call, specify three arguments, corresponding to the worker number, the IP for registry" \
              ", and the local IP."
        quit()

    set_context()
    address = 'http://' + sys.argv[3] + ':600' + str(sys.argv[1])
    host = create_host(address)

    registry_address = 'http://' + sys.argv[2] + ':5999/registry'
    registry = host.lookup_url(registry_address, 'Registry', 'Registry')
    name = 'worker' + str(sys.argv[1])
    registry.bind(name, host)
    serve_forever()
