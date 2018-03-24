""""
Common definitions for functions
Authors: Amanda Gomez Gomez, Oussama El Azizi
"""

import unicodedata, urllib


def get_file_words(file, http_server, red_func, reducer):
    punc = ',.!?-*&^%$#@[]()'
    mapped_words=[]
    # Assuming the file already exists
    print "Downloading "+file
    file_name,_ = urllib.urlretrieve(http_server+'/parted/'+file, filename=file)
    print "Download done"
    reducer.set_init_time()
    print "Processing Starts"
    # Map and send to reduce in the same loop
    with open(file_name) as contents:
        for line in contents:
            out_of_punc = map(lambda x: remove_accent_mark(x.strip(punc).lower()), line.split())
            mapped_words = filter(lambda x: x != '', out_of_punc)
            if len(mapped_words) > 0:
                reducer.reduce(mapped_words, red_func)

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


def outputFormat(data):
    return 'Results: \n---------------------------\nTotal: '+str(data['total'])


