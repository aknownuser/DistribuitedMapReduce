"""
Reducer to be binded to the registry and later used for the Reducing stage
Authors: Amanda Gomez Gomez, Oussama El Azizi
"""
from collections import Counter
from pyactor.context import set_context, create_host, serve_forever, sleep, shutdown
import functionsMapRed as fmr


class Reduce(object):
    _tell = ['set_mappers_num', 'reduce']

    def __init__(self):
        self.mappers = 0
        self.data = Counter()

    def set_mappers_num(self, mappers_num):
        self.mappers = mappers_num

    def reduce(self, list, func):
        self.data = func(self.data, list)
        self.mappers -=1
        if self.mappers == 0:
            print self.data


if __name__ == "__main__":
    set_context()
    host = create_host('http://192.168.1.43:6100/')

    registry = host.lookup_url('http://192.168.1.39:5999/registry', 'Registry', 'Registry')
    registry.bind('reducer', host)


    serve_forever()