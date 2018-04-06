""""
Common definitions for functions
Authors: Amanda Gomez Gomez, Oussama El Azizi
"""
from collections import Counter
import unicodedata, urllib2, time, urllib

def get_file_words(file, http_server, reducer):
    punc = ',.:!?-_\'*&^%$#@[]()'
    mapped_words = Counter()
    # Assuming the file already exists
    print "Downloading "+file
    file_name,_ = urllib.urlretrieve(http_server+'/parted/'+file, filename=file)
    print "Download done"
    reducer.set_init_time()
    print "Processing Starts"
    with open(file_name) as contents:
        for line in contents:
            mapped_words.update(filter(lambda x: x != '', map(lambda x: x.strip(punc).lower(), line.split())))
    print "Processing Done"
    return mapped_words



def word_count(data, list):

    data.update(list)
    print '.'
    return data


def counting_words(data, list):
    data['total'] = data['total']+sum(list.values())
    print '.'
    return data


def outputFormat(data, func):
    if func.__name__ == 'word_count':
        return 'Results for word_count\n---------------------------\nFrequencies are:\n'+str(data)
    return 'Results for counting words\n---------------------------\nTotal count of words: '+str(data['total'])


