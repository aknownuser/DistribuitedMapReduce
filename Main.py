"""
Main program that spawns the Mappers and initializes their execution
Authors: Amanda Gomez Gomez, Oussama El Azizi
"""

from pyactor.context import set_context, create_host,shutdown
import functionsMapRed as fmr
import os, sys


def split_file(file_name, num):

    lines = open(file_name).readlines()
    file_len = len(lines)/num
    i = 1
    for line_num in range(0, len(lines), file_len):
        if i > num: break
        data = lines[line_num:line_num+file_len]
        output = open('parted/part'+str(i), 'w')
        output.writelines(data)
        del data
        output.close()
        i = i + 1


if __name__ == "__main__":
    if len(sys.argv) != 4:
        print "Error, you should specify 3 parameters: the name of the file to process, the registry's IP and the local IP."
        quit()


    set_context()
    address = 'http://' + sys.argv[3] + ':12345'
    host = create_host(address)

    registry_address = 'http://' + sys.argv[2] + ':5999/registry'
    registry = host.lookup_url(registry_address, 'Registry', 'Registry')

    reducer_host = registry.lookup('reducer')
    reducer = reducer_host.spawn('reducer', 'Reducer/Reduce')

    mappers = registry.get_all()
    worker = []
    i = 0
    for mapper in mappers:
        worker.append(mapper.spawn('mapper', 'Mapper/Map'))
        worker[i].set_http_server('http://'+sys.argv[3])
        i = i+1
    reducer.set_mappers_num(i)

    split_file(sys.argv[1], i)
    i = 0

    for wor in worker:
        wor.map(i+1, reducer, fmr.get_file_words, fmr.word_count)
        i = i + 1

    shutdown()
