#!/bin/python

import math
import os
import random
import re
import sys


#
# Complete the 'reverse_words_order_and_swap_cases' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING sentence as parameter.
#

def reverseWords(sentence):
    words = []
    word = ''
    count = 0
    for elem in sentence:
        if elem != ' ':            
            word += elem
            if count == len(sentence) - 1:
                words.append(word)
        else:
            words.append(word)
            word = ''
        count += 1
    reversedList = list(reversed(words))
    words = ' '.join(reversedList)
    return words

def swapCases(sentence):
    newSentence = []
    for elem in sentence:
        if elem.isupper():
            elem = elem.lower()
            newSentence += elem
        else:
            elem = elem.upper()
            newSentence += elem
        newSentence = ''.join(newSentence)
    return newSentence

def reverse_words_order_and_swap_cases(sentence):
    sentence = reverseWords(sentence)
    result = swapCases(sentence)
    return result
    # Write your code here
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    sentence = raw_input()

    result = reverse_words_order_and_swap_cases(sentence)

    fptr.write(result + '\n')

    fptr.close()
