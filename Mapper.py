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
    _tell = ['map']
    _ref = ['map']

    def map(self, i, reducer, function, map_func):

        file = 'part' + str(i)
        mapped_words = map_func(file)
        reducer.reduce(mapped_words, function)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print "Incorrect call, specify one argument, corresponding to the worker number."
        quit()

    set_context()
    address = 'http://127.0.0.1:600'+str(sys.argv[1])
    host = create_host(address)

    registry = host.lookup_url('http://127.0.0.1:5999/registry', 'Registry', 'Registry')
    name = 'worker'+str(sys.argv[1])
    registry.bind(name, host)
    serve_forever()