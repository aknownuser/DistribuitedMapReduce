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
    _tell = ['map','map_r','mapI']
    _ref = ['map','map_r','mapI']

    def map(self, func, data, reducer, reduce_func, init):
        data_mapped = Counter()
        #Do map and create the dictionary
        data_mapped= data_mapped.update(map(func, data))
        #Start reducer
        reducer.reduce(reduce_func, data_mapped, init)

    def map_r(self, i, reducer, reduce_func, reduce_init):
        self.reducer = reducer
        mapped_words = []
        data_dict = Counter()
        punc = ',.!?-*&^%$#@'
        file = 'part'+str(i)
        print file
        # Assuming the file already exists
        with open(file) as f:
            for line in f:
                #Apply map determened map function
                mapped_words = mapped_words + map(lambda x: x.rstrip(punc).lower(), line.split())
        print mapped_words
        #Update Dictionary
        data_dict.update(mapped_words)
        # Send the result to the reducer
        self.reducer.reduce(reduce_func, data_dict, reduce_init)

    def map(self, i, reducer, reduce_mode):
        self.reducer = reducer
        mapped_words = []
        punc = ',.!?-*&^%$#@'
        file = 'part'+str(i)
        print file
        # Assuming the file already exists
        with open(file) as f:
            for line in f:
                mapped_words = mapped_words + map(lambda x: x.rstrip(punc).lower(), line.split())
        print mapped_words

        # Send the result to the reducer
        if reduce_mode == "counting_words":
            self.reducer.counting_words(mapped_words)
        if reduce_mode == "word_count":
            self.reducer.word_count(mapped_words)

    def mapI(self, i, reducer, function):
        self.reducer = reducer
        mapped_words = []
        punc = ',.!?-*&^%$#@'
        file = 'part' + str(i)
        print file
        # Assuming the file already exists
        with open(file) as f:
            for line in f:
                mapped_words = mapped_words + map(lambda x: x.rstrip(punc).lower(), line.split())
        print mapped_words
        self.reducer.reduce(mapped_words, function)

if __name__ == "__main__":
    if (len(sys.argv) != 2):
        print "Incorrect call, specify one argument, corresponding to the worker number."
        quit()

    set_context()
    address = 'http://127.0.0.1:600'+str(sys.argv[1])
    host = create_host(address)

    registry = host.lookup_url('http://127.0.0.1:5999/registry', 'Registry', 'Registry')


    name = 'worker'+str(sys.argv[1])
    registry.bind(name, host)


    serve_forever()