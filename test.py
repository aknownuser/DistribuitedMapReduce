"""
unittest

Authors: Amanda Gomez Gomez, Oussama El Azizi
"""

import unittest

from pyactor.context import set_context, create_host, shutdown
from Mapper import Map
from Reducer import Reduce
from Registry import Registry
import functionsMapRed as fmr
import sys
import time


class Outs(object):

    """
    Class that controls the stdou.
    """
    lines = []

    def write(self, line):
        """
        Function that stores the lines of sdtout.
        :param line: line to be stored
        :return:
        """

        if line == '\n':
            line_split = map(lambda x: x + '\n', self.lines.pop().split('\n'))
            self.lines += line_split
        else:
            self.lines.append(line)

    def clear(self):
        """
        Clears the stdout lines.
        :return:
        """
        self.lines = []


class MyTestCase(unittest.TestCase):

    """
    Testing class.
    """

    def setUp(self):
        set_context()
        self.maxDiff = None
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
        self.out.clear()

    def test_frequencies(self):
        """
        Tests the frequencies.
        :return:
        """
        self.out.clear()
        self.reduce.set_mappers_num(1)
        self.mapper.map(-1, self.reduce, fmr.get_file_words, fmr.word_count)
        time.sleep(2)
        self.assertListEqual(self.out.lines[:-1], open('wordCount', 'r').readlines()[:-1])

    def test_count_words(self):
        """
        Tests the word count.
        :return:
        """
        self.out.clear()
        self.reduce.set_mappers_num(1)
        self.mapper.map(-1, self.reduce, fmr.get_file_words, fmr.counting_words)
        time.sleep(2) 
        self.assertListEqual(self.out.lines[:-1], open('count', 'r').readlines()[:-1])

    def test_unbind_all(self):
        """
        Test the bind and unbind in the registry.
        :return:
        """
        self.registry.unbind('reducer')
        self.registry.unbind('mapper')
        self.assertRaises(KeyError, self.registry.lookup, 'reducer')
        self.assertEqual(self.registry.lookup('mapper'), None)
        self.assertListEqual(self.registry.get_all(), [])


if __name__ == '__main__':
    print ('## Run the tests.')

    suite = unittest.TestLoader().loadTestsFromTestCase(MyTestCase)
    unittest.TextTestRunner(verbosity=2).run(suite)
