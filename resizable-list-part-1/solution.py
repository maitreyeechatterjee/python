"""
Problem: Resizable List Part 1
URL: https://neetcode.io/problems/python-resizable-list-part-1/question
Language: python

Solution by NeetCode GitHub Pusher
"""

from typing import Listfrom typing import List


def append_elements(arr1: List[int], arr2: List[int]) -> List[int]:def append_elements(arr1: List[int], arr2: List[int]) -> List[int]:
    for item in arr2:    for item in arr2:
        arr1.append(item)        arr1.append(item)
    return arr1    return arr1

