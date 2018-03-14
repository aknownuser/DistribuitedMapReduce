"""
Main program that spawns the Mappers and initializes their execution
Authors: Amanda Gomez Gomez, Oussama El Azizi
"""

from pyactor.context import set_context, create_host, sleep, shutdown
import functionsMapRed as fmr


if __name__ == "__main__":
    set_context()
    host = create_host('http://127.0.0.1:12345')

    registry = host.lookup_url('http://127.0.0.1:5999/registry', 'Registry', 'Registry')

    reducer_host = registry.lookup('reducer')
    reducer = reducer_host.spawn('reducer', 'Reducer/Reduce')


    mappers = registry.get_all()
    worker = []
    i = 0
    for mapper in mappers:
        worker.append(mapper.spawn('mapper', 'Mapper/Map'))
        i = i+1
    reducer.set_mappers_num(i)
    print i
    i = 0
    for wor in worker:
        wor.mapI(i+1, reducer, fmr.counting_words)
        i = i + 1


    shutdown()
