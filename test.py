import unittest

from pyactor.context import set_context, create_host, sleep, shutdown
from Mapper import Map
from Reducer import  Reduce
from Registry import Registry
import functionsMapRed as fmr
import sys, time

class Outs(object):

    lines =""

    def write(self, line):

        self.lines += line

    def clear(self):

        self.lines=""

class MyTestCase(unittest.TestCase):

    def setUp(self):
        set_context()

        self.h = create_host()
        self.registry = self.h.spawn('Registry', Registry)

        self.mapper = self.h.spawn('Map', Map)
        self.mapper.set_http_server('http://127.0.0.1')

        self.reduce = self.h.spawn('Reduce', Reduce)

        self.registry.bind('reducer', self.reduce)
        self.registry.bind('mapper', self.mapper)
        self.stdo = sys.stdout

        self.out = Outs()

        sys.stdout = self.out


    def tearDown(self):
        shutdown()

    def test_frequencies(self):
        self.reduce.set_mappers_num(1)
        self.mapper.map(-1, self.reduce,fmr.get_file_words, fmr.word_count)
        time.sleep(2)
        self.assertEqual(self.out.lines, open('wordCount', 'r').read())

    def test_countwords(self):
        self.reduce.set_mappers_num(1)
        self.mapper.map(-1, self.reduce, fmr.get_file_words, fmr.counting_words)
        time.sleep(2)
        self.assertEqual(self.out.lines, open('count','r').read())

    def test_unbindall(self):
        self.registry.unbind('reducer')
        self.registry.unbind('mapper')
        self.assertRaises(KeyError, self.registry.lookup,'reducer')
        self.assertListEqual(self.registry.get_all(), [])


if __name__ == '__main__':
    print ('## Run the tests.')

    suite = unittest.TestLoader().loadTestsFromTestCase(MyTestCase)
    unittest.TextTestRunner(verbosity=2).run(suite)

