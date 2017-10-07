#!/usr/bin/env python
# coding=utf-8

import string, re


def count_word(filename):
    f = open(filename, 'rb')
    wdic = {}
    for line in f:
        line = line.lower().strip()
        #split by regular expression, more powerful function
        words = re.split('\W+', line)
        #words = re.findall('[a-zA-Z0-9]+', line)

        for word in words:
            if word in wdic:
                wdic[word] += 1
            else:
                wdic[word] = 1
    f.close()
    items = wdic.items()
    wordList = sorted(items, key = lambda item: item[1], reverse = True)
    print wordList

if __name__ == '__main__':
    filename = 'testEnglish.txt'
    count_word(filename)





