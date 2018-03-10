"""
Main program that spawns the Mappers and initializes their execution
Authors: Amanda Gomez Gomez, Oussama El Azizi
"""

from pyactor.context import set_context, create_host, sleep, shutdown

if __name__ == "__main__":
    set_context()
    host = create_host('http://127.0.0.1:12345')

    registry = host.lookup_url('http://127.0.0.1:6000/registry', 'Registry', 'Registry')

    reducer_host = registry.lookup('reducer')
    reducer = reducer_host.spawn('reducer', 'Reducer/Reduce')

    mappers = registry.get_all()

    i = 1
    for mapper in mappers:
        worker = mapper.spawn('mapper', 'Mapper/Map')
        worker.map(i, reducer, "counting_words")
        i = i+1
        reducer.set_mappers_num(i)


    shutdown()
