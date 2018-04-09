import time
from collections import Counter
import sys
import os


def word_count(f):
    """
    Word count sequential.
    :param f: file to process
    :return: frequencies
    """
    word_dict = Counter()
    punc = ',.:;!?-_\'\"+=/*&^%$#@[]()'
    #  with will automatically close your file
    with open(f) as in_file:
        # iterate over each line
        for line in in_file:
            # pass each stripped word from the line to the Counter dict
            mapped_words = [val for val in [x_val.strip(punc).lower() for x_val in line.split()]
                            if val != '']
            word_dict.update(mapped_words)
    return word_dict


def counting_word(file_name):
    """
    Counting word sequential.
    :param file_name: file to be process.
    :return: number of words.
    """
    count = 0
    punc = ',.:;!?-_\'\"+=/*&^%$#@[]()'
    with open(file_name) as file_name:
        for line in file_name:
            count = count + len([val for val in [x_val.strip(punc).lower() for x_val in line.split()]
                                 if val != ''])
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
        print counting_word(x)
        elapsed_time = time.time() - start_time
        print "Elapsed time: " + str(elapsed_time)

        print "----------WORD COUNT----------"
        print str(x) + ": " + " Size: " + str(statinfo.st_size)
        start_time = time.time()
        print word_count(x)
        elapsed_time = time.time() - start_time
        print "Elapsed time: " + str(elapsed_time)
