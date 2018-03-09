"""
Workers to be binded to the registry and later used to spawn Mappers
The call takes 1 parameter, to specify the number of the worker
Authors: Amanda Gomez Gomez, Oussama El Azizi
"""
import sys
from pyactor.context import set_context, create_host, serve_forever, sleep, shutdown

class Map(object):
    _tell = ['map']
    _ref = ['map']

    def map(self, i, reducer):
        self.reducer = reducer
        file = 'part'+str(i)
        print file

        # Assuming the file already exists
        f = open(file)
        lines = f.readlines()
        print lines
        f.close()

        # Send the result to the reducer
        self.reducer.sayHello()


if __name__ == "__main__":
    if (len(sys.argv) != 2):
        print "Incorrect call, specify one argument, corresponding to the worker number."
        quit()

    set_context()
    address = 'http://127.0.0.1:600'+str(sys.argv[1])
    host = create_host(address)

    registry = host.lookup_url('http://127.0.0.1:6000/registry', 'Registry', 'Registry')


    name = 'worker'+str(sys.argv[1])
    registry.bind(name, host)


    serve_forever()