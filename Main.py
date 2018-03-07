import re, time

def counting_word(file_name):
    count = 0
    with open(file_name) as file:
        for line in file:
            print list(filter(lambda x: x != '' and x != '\n', re.split("\W+", line)))
            count = count + len(list(filter(lambda x: x != '' and x != '\n', re.split("\W+", line))))
    return count

def counting_word_isallnum(file_name):
    count=0
    with open(file_name)  as file:
        for line in file:
            line.isalnum()
            pass


def word_count(file_name):
    dict={}

    with open(file_name) as file:
        for line in file:
            words = list(filter(lambda x: x != '' and x != '\n', re.split("\W+", line)))

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