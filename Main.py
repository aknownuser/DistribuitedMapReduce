import time
import functools
from collections import Counter

def word_count(f):
    word_dict = Counter()
    punc = ',.!?-*&^%$#@'
    #  with will automatically close your file
    with open(f) as in_file:
        # iterate over each line
        for line in in_file:
            # pass each stripped word from the line to the Counter dict
            mapped_words = map(lambda x :x.rstrip(punc).lower(), line.split())
            word_dict.update(mapped_words)
    return word_dict

def counting_word(file_name):
    count = 0
    punc = ',.!?-*&^%$#@'
    with open(file_name) as file:
        for line in file:
            line = map(lambda x: x.rstrip(punc).lower(),line.split())
            count = count + len(filter(lambda x: x != '' and x != '\n',line))
    return count

if __name__ == "__main__":
    #print "----------COUNT WORDS-----------"
    #start_time = time.time()
    #print "Sherlok Holmes: "+str(counting_word("big.txt"))
    #elapsed_time = time.time() - start_time
    #print "Elapsed time: "+str(elapsed_time)

    #start_time = time.time()
    #print "\nEl Quijote: " + str(counting_word("pg2000.txt"))
    #elapsed_time = time.time() - start_time
    #print "Elapsed time: " + str(elapsed_time)
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
    print "\nEl Quijote: \n" + str(word_count("pg2000.txt"))
    elapsed_time = time.time() - start_time
    print "Elapsed time: " + str(elapsed_time)
    # PG10.txt
    #start_time = time.time()
    #print "\nThe bible: \n" + str(word_count("pg10.txt"))
    #elapsed_time = time.time() - start_time
    #print "Elapsed time: " + str(elapsed_time)
    #print "------------------------------"