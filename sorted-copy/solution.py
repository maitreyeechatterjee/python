"""
Problem: Sorted Copy
URL: https://neetcode.io/problems/python-sorted-copy/question
Language: python

Solution by NeetCode GitHub Pusher
"""


def sort_numbers(numbers: List[int]) -> List[int]:def sort_numbers(numbers: List[int]) -> List[int]:
    sorted_numbers = sorted(numbers, key=abs, reverse=True)    sorted_numbers = sorted(numbers, key=abs, reverse=True)
    return(sorted_numbers)    return(sorted_numbers)


# do not modify below this line# do not modify below this line
original_words = ["cherry", "apple", "blueberry", "banana", "watermelon", "zucchini", "kiwi", "pear"]original_words = ["cherry", "apple", "blueberry", "banana", "watermelon", "zucchini", "kiwi", "pear"]

print(original_words)print(original_words)