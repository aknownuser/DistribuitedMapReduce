"""
Reducer to be binded to the registry and later used for the Reducing stage
Authors: Amanda Gomez Gomez, Oussama El Azizi
"""
from collections import Counter
import time, sys
from pyactor.context import set_context, create_host, serve_forever, sleep, shutdown
import functionsMapRed as fmr


class Reduce(object):
    _tell = ['set_mappers_num', 'set_init_time', 'reduce']

    def __init__(self):
        self.mappers = 0
        self.data = Counter()
        self.init_time = 0

    def set_mappers_num(self, mappers_num):
        self.mappers = mappers_num

    def set_init_time(self):
        if self.init_time == 0:
            self.init_time = time.time()

    def reduce(self, list, func):
        self.data = func(self.data, list)
        self.mappers -=1
        if self.mappers == 0:
            print fmr.outputFormat(self.data, func)
            print 'MapReduce completed in '+str(time.time() - self.init_time)+ ' seconds'


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print "Incorrect call, specify two arguments, corresponding to the IP for registry and the local IP."
        quit()

    set_context()
    address = 'http://' + sys.argv[2] + ':6100'
    host = create_host(address)

    registry_address = 'http://' + sys.argv[1] + ':5999/registry'
    registry = host.lookup_url(registry_address, 'Registry', 'Registry')
    registry.bind('reducer', host)


    serve_forever()