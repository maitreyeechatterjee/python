"""
Problem: Sort Lambda
URL: https://neetcode.io/problems/python-sort-lambda/question
Language: python

Solution by NeetCode GitHub Pusher
"""

from typing import Listfrom typing import List


def sort_words(words: List[str]) -> List[str]:def sort_words(words: List[str]) -> List[str]:
    return sorted(words, key=lambda word: len(word), reverse=True)    return sorted(words, key=lambda word: len(word), reverse=True)


def sort_numbers(numbers: List[int]) -> List[int]:def sort_numbers(numbers: List[int]) -> List[int]:
    return sorted(numbers, key= abs)    return sorted(numbers, key= abs)


# do not modify below this line# do not modify below this line
print(sort_words(["cherry", "apple", "blueberry", "banana", "watermelon", "zucchini", "kiwi", "pear"]))print(sort_words(["cherry", "apple", "blueberry", "banana", "watermelon", "zucchini", "kiwi", "pear"]))

print(sort_numbers([1, -5, -3, 2, 4, 11, -19, 9, -2, 5, -6, 7, -4, 2, 6]))print(sort_numbers([1, -5, -3, 2, 4, 11, -19, 9, -2, 5, -6, 7, -4, 2, 6]))
