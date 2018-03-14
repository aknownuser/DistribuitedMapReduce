""""
Common definitions for functions
"""
from collections import Counter

def word_count(self, data, list):
    word_dict = Counter()
    word_dict.update(data)
    print word_dict


def counting_words(data, list):
    data['total'] = data['total']+len(list)
    return data