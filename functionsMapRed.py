""""
Common definitions for functions
"""
from collections import Counter

def word_count(data, list):
    data.update(list)
    return data


def counting_words(data, list):
    data['total'] = data['total']+len(list)
    return data