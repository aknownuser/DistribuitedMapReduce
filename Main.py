import time
import functools
from collections import Counter
import unicodedata, sys

def remove_accent_mark(s):
    s = s.decode('utf-8')
    result = ''.join((c for c in unicodedata.normalize('NFD', s) if unicodedata.category(c) != 'Mn'))
    return result.encode('utf-8')

def word_count(f):
    word_dict = Counter()
    punc = ',.!?-*&^%$#@[]'
    #  with will automatically close your file
    with open(f) as in_file:
        # iterate over each line
        for line in in_file:
            # pass each stripped word from the line to the Counter dict
            mapped_words =filter(lambda x: x != '', map(lambda x: remove_accent_mark(x.strip(punc).lower()), line.split()))
            word_dict.update(mapped_words)
    return word_dict

def counting_word(file_name):
    count = 0
    punc = ',.!?-*&^%$#@'
    with open(file_name) as file:
        for line in file:
            count = count + len(filter(lambda x: x != '', map(lambda x: remove_accent_mark(x.strip(punc).lower()), line.split())))
    return count

if __name__ == "__main__":

    if len(sys.argv) != 2:
        print "Not enough paramaters: You need to put the files name."

    print "----------COUNT WORDS-----------"
    #start_time = time.time()
    #print "Sherlok Holmes: "+str(counting_word("big.txt"))
    #elapsed_time = time.time() - start_time
    #print "Elapsed time: "+str(elapsed_time)

    start_time = time.time()
    print "\nEl Quijote: " + str(counting_word(sys.argv[1]))
    elapsed_time = time.time() - start_time
    print "Elapsed time: " + str(elapsed_time)
    #PG10.txt
    #start_time = time.time()
    #print "\nThe bible: "+str(counting_word("pg10.txt"))
    #elapsed_time = time.time() - start_time
    #print "Elapsed time: " + str(elapsed_time)
    #print "-------------------------------"

    print "\n----------WORD COUNT----------"
    #start_time = time.time()
    #print "Sherlok Holmes: \n" + str(word_count("big.txt"))
    #elapsed_time = time.time() - start_time
    #print "Elapsed time: " + str(elapsed_time)

    start_time = time.time()
    print "\nEl Quijote: \n" + str(word_count(sys.argv[1]))
    elapsed_time = time.time() - start_time
    print "Elapsed time: " + str(elapsed_time)
    # PG10.txt
    #start_time = time.time()
    #print "\nThe bible: \n" + str(word_count("pg10.txt"))
    #elapsed_time = time.time() - start_time
    #print "Elapsed time: " + str(elapsed_time)
    #print "------------------------------"