""""
Common definitions for functions
"""
from collections import Counter


def get_file_words(file):
    punc = ',.!?-*&^%$#@'
    mapped_words=[]
    # Assuming the file already exists
    with open(file) as f:
        for line in f:
            mapped_words = mapped_words + map(lambda x: x.rstrip(punc).lower(), line.split())
    return mapped_words


def word_count(data, list):

    data.update(list)
    return data


def counting_words(data, list):
    data['total'] = data['total']+len(list)
    return data
