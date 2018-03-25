""""
Common definitions for functions
Authors: Amanda Gomez Gomez, Oussama El Azizi
"""
from collections import Counter
import unicodedata, urllib2, time, urllib

def get_file_words(file, http_server, reducer):
    punc = ',.!?-*&^%$#@[]()'
    mapped_words = Counter()
    # Assuming the file already exists
    print "Downloading "+file
    #contents = urllib2.urlopen(http_server+'/parted/'+file)
    file_name,_ = urllib.urlretrieve(http_server+'/parted/'+file, filename=file)
    print "Download done"
    #print contents
    reducer.set_init_time()
    print "Processing Starts"
    with open(file_name) as contents:
        for line in contents:
            mapped_words.update(filter(lambda x: x != '', map(lambda x: remove_accent_mark(x.strip(punc).lower()), line.split())))
    print "Processing Done"
    return mapped_words


def remove_accent_mark(s):
    s = s.decode('utf-8')
    result = ''.join((c for c in unicodedata.normalize('NFD', s) if unicodedata.category(c) != 'Mn'))
    return result.encode('utf-8')

def word_count(data, list):

    data.update(list)
    print '.'
    return data


def counting_words(data, list):
    data['total'] = data['total']+len(list)
    print '.'
    return data


def outputFormat(data, func):
    if func.__name__ == 'word_count':
        return 'Results for word_count\n---------------------------\nFrequencies are:\n'+str(data)
    return 'Results for counting words\n---------------------------\nTotal count of words: '+str(data['total'])


