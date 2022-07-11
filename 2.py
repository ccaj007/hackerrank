from importlib.machinery import WindowsRegistryFinder
import math
import os
import random
import re
import sys
import itertools


#
# Complete the 'transformSentence' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING sentence as parameter.
#
"""
There is a sentence that consists of space-separated strings of upper and lower case
English letters. Transform each string according to the given algorithm and return
the new sentence.

Each string should be modified as follows:

- the first character of the string remains unchanged
- for each subsequent character, say x, consider a letter preceding it, say y:
    - if y precedes x in the English alphabet, transfor x to uppercase
    - if x precedes y in the English alphabes, transfor x to lowercase
    - if x and y are equal, the letter remains unchanged

ex:
a Blue MOON
a BLUe MOOn

ab cB GG
aB cb GG

x y z
x y z
"""

def transformSentence(sentence):
    # Write your code here
    words = sentence.split(" ")
    for word in words:        
        #new_word = ""
        if len(word) == 0 or len(word) == 1:
            new_word = word
        else:          
            new_word = word[0]
            for i in range(0,len(word)-1):
                char1 = word[i]
                char2 = word[i+1]

                print(char1, char2)
                # if char1.lower > char2.lower:

                print(new_word)


def main():
    transformSentence("a Blue MOON")

if __name__ == '__main__':
#    fptr = open(os.environ['OUTPUT_PATH'], 'w')
#
#    sentence = input()
#
#    result = transformSentence(sentence)
#
#    fptr.write(result + '\n')
#
#    fptr.close()

    main()