""""
Common definitions for functions
Authors: Amanda Gomez Gomez, Oussama El Azizi
"""
from collections import Counter


def get_file_words(file):
    punc = ',.!?-*&^%$#@[]()'
    mapped_words=[]
    # Assuming the file already exists
    with open(file) as f:
        for line in f:
            mapped_words = mapped_words + filter(lambda x: x != '', map(lambda x: x.strip(punc).lower(), line.split()))

    print mapped_words
    return mapped_words


def word_count(data, list):

    data.update(list)
    return data


def counting_words(data, list):
    data['total'] = data['total']+len(list)
    return data


def outputFormat(data, func):
    if func.__name__ == 'word_count':
        return 'Results for word_count\n---------------------------\nFrequencies are:\n'+str(data)
    return 'Results for counting words\n---------------------------\nTotal count of words: '+str(data['total'])


