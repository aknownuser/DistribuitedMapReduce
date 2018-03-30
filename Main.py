import time
from collections import Counter
import unicodedata, sys, os

def remove_accent_mark(s):
    s = s.decode('utf-8')
    result = ''.join((c for c in unicodedata.normalize('NFD', s) if unicodedata.category(c) != 'Mn'))
    return result.encode('utf-8')

def word_count(f):
    word_dict = Counter()
    punc = ',.!?-*&^%$#@[]()'
    #  with will automatically close your file
    with open(f) as in_file:
        # iterate over each line
        for line in in_file:
            # pass each stripped word from the line to the Counter dict
            mapped_words =filter(lambda x: x != '', map(lambda x: x.strip(punc).lower(), line.split()))
            word_dict.update(mapped_words)
    return word_dict

def counting_word(file_name):
    count = 0
    punc = ',.!?-*&^%$#@[]()'
    with open(file_name) as file:
        for line in file:
            count = count + len(filter(lambda x: x != '', map(lambda x: x.strip(punc).lower(), line.split())))
    return count

if __name__ == "__main__":

    if len(sys.argv) <= 1:
        print "Not enough paramaters: You need to put the files name."
    i = 0
    for x in sys.argv:
        if i == 0:
            i = 1
            continue
        statinfo = os.stat(x)
        print "----------COUNT WORDS-----------"
        print str(x) + ": " + " Size: "+str(statinfo.st_size)
        start_time = time.time()
        counting_word(x)
        elapsed_time = time.time() - start_time
        print "Elapsed time: " + str(elapsed_time)

        print "----------WORD COUNT----------"
        print str(x) + ": " + " Size: " + str(statinfo.st_size)
        start_time = time.time()
        word_count(x)
        elapsed_time = time.time() - start_time
        print "Elapsed time: " + str(elapsed_time)