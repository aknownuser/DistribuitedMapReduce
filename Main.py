import re, time
from collections import Counter

def word_count(f):
    word_dict = Counter()
    punc = ',.!?-*&^%$#@'
    #  with will automaticlly close your file
    with open(f) as in_file:
        # iterate over each line
        for line in in_file:
            # pass each stripped word from the line to the Counter dict
            word_dict.update(x.rstrip(punc).lower() for x in line.split())
    return word_dict

def counting_word(file_name):
    count = 0
    punc = ',.!?-*&^%$#@'
    with open(file_name) as file:
        for line in file:
            print list(filter(lambda x: x != '' and x != '\n', re.split("\W+", line)))
            count = count + len(list(filter(lambda x: x != '' and x != '\n',re.split("\W+", line))))
    return count

if __name__ == "__main__":


    start_time = time.time()
    print counting_word("simple.txt")
    elapsed_time = time.time() - start_time
    print "time: "+str(elapsed_time)

    """  
    start_time = time.time()
    print counting_word("pg10.txt")
    elapsed_time = time.time() - start_time
    print "time: " + str(elapsed_time)

    start_time = time.time()
    print counting_word("pg2000.txt")
    elapsed_time = time.time() - start_time
    print "time: " + str(elapsed_time)
    """