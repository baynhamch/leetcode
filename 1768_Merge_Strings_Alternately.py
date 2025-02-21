"""
1768. Merge String Alternately

You are given two strings word1 and word2. Merge the strings by adding letters in alternating order, starting with word1. If a string is longer than the other, append the additional letters onto the end of the merged string.

Return the merged string.
Link:
https://leetcode.com/problems/merge-strings-alternately/description/?envType=study-plan-v2&envId=leetcode-75
"""
word1 = "abc"
word2 = "pqr"
word_list = []

for i in range(min(len(word1), len(word2))):
    word_list.append(word1[i])
    word_list.append(word2[i])

if len(word1) > len(word2):
    word_list.append(word1[len(word2):])
else:
    word_list.append(word2[len(word1):])

# print("".join(word_list))

from itertools import zip_longest

def merge_alternately(word1: str, word2: str) -> str:
    return ''.join(a + b if a and b else a or b for a, b in zip_longest(word1, word2, fillvalue=''))


print(merge_alternately("abc", "pqr"))
print(merge_alternately("ab", "pqrs"))
print(merge_alternately("abcd", "pq"))
