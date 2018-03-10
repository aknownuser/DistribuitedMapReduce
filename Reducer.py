"""
Reducer to be binded to the registry and later used for the Reducing stage
Authors: Amanda Gomez Gomez, Oussama El Azizi
"""
import sys
from collections import Counter
from pyactor.context import set_context, create_host, serve_forever, sleep, shutdown

class Reduce(object):
    _tell = ['sayHello', 'word_count', 'counting_words', 'set_mappers_num']

    def __init__(self):
        self.mappers=0

    def set_mappers_num(self, mappers_num):
        self.mappers = mappers_num

    def reduce(self, func, data, init):
        if data.empty():
            return init
        else:
            func(data.pop(), self.reduce(func, data, init))

    def word_count(self, data):
        word_dict = Counter()
        word_dict.update(data)
        print word_dict

    def counting_words(self, data):
        print len(filter(lambda x: x != '' and x != '\n',data))

if __name__ == "__main__":

    set_context()
    host = create_host('http://127.0.0.1:6100')

    registry = host.lookup_url('http://127.0.0.1:6000/registry', 'Registry', 'Registry')
    registry.bind('reducer', host)


    serve_forever()