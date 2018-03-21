"""
Workers to be binded to the registry and later used to spawn Mappers
The call takes 1 parameter, to specify the number of the worker
Authors: Amanda Gomez Gomez, Oussama El Azizi
"""
import sys

from pyactor.context import set_context, create_host, serve_forever, sleep, shutdown
from collections import Counter
import functionsMapRed as fmr


class Map(object):
    _tell = ['map', 'set_http_server']
    _ref = ['map']

    def map(self, i, reducer, map_func, red_func):

        file = 'part' + str(i)
        mapped_words = map_func(file, self.http_server)
        reducer.reduce(mapped_words, red_func)

    def set_http_server(self, addr):
        self.http_server = addr+':8000'

if __name__ == "__main__":
    if len(sys.argv) != 4:
        print "Incorrect call, specify three arguments, corresponding to the worker number, the IP for registry, and the local IP."
        quit()

    set_context()
    address = 'http://' + sys.argv[3] + ':600'+str(sys.argv[1])
    host = create_host(address)

    registry_address = 'http://'+sys.argv[2]+':5999/registry'
    registry = host.lookup_url(registry_address, 'Registry', 'Registry')
    name = 'worker'+str(sys.argv[1])
    registry.bind(name, host)
    serve_forever()