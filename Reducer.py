"""
Reducer to be binded to the registry and later used for the Reducing stage
Authors: Amanda Gomez Gomez, Oussama El Azizi
"""
import sys
from pyactor.context import set_context, create_host, serve_forever, sleep, shutdown

class Reduce(object):
    _tell = ['sayHello']

    def sayHello(self):
        print "Hi, this is the reducer"


if __name__ == "__main__":

    set_context()
    host = create_host('http://127.0.0.1:6100')

    registry = host.lookup_url('http://127.0.0.1:6000/registry', 'Registry', 'Registry')
    registry.bind('reducer', host)


    serve_forever()