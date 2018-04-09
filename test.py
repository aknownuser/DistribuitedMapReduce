import unittest
import Main
from collections import Counter


class MyTestCase(unittest.TestCase):
    """
    Class to test sequential.
    """

    def test_counting_words(self):
        """
        Counting Words test.
        :return:
        """
        values = Counter({'es': 3, 'prueba': 2, 'cosas': 2, 'peque\xc3\x91o': 2, 'este': 1, 'en': 1,
                          'nuevas': 1, 'llano': 1, 'muy': 1, 'de': 1, 'por': 1, 'texto': 1, 'alal': 1,
                          'repito': 1, 'y': 1, 'eso': 1, 'aunque': 1, 'caste': 1})
        values_to_test = Main.word_count('part-1')
        self.assertDictEqual(values_to_test, values)

    def test_word_count(self):
        """
        Word Count test.
        :return:
        """
        value_to_test = Main.counting_word('part-1')
        self.assertEqual(value_to_test, 23)


if __name__ == '__main__':
    print ('## Run the tests.')

    suite = unittest.TestLoader().loadTestsFromTestCase(MyTestCase)
    unittest.TextTestRunner(verbosity=2).run(suite)
