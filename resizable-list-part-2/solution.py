"""
Problem: Resizable List Part 2
URL: https://neetcode.io/problems/python-resizable-list-part-2/question
Language: python

Solution by NeetCode GitHub Pusher
"""

def append_elements(arr1: List[int], arr2: List[int]) -> List[int]:def append_elements(arr1: List[int], arr2: List[int]) -> List[int]:
    arr1.extend(arr2)    arr1.extend(arr2)
    return arr1    return arr1
    

def remove_elements(arr1: List[int], arr2: List[int]) -> List[int]:def remove_elements(arr1: List[int], arr2: List[int]) -> List[int]:
    for element in arr2:    for element in arr2:
        if element in arr1:        if element in arr1:
            arr1.remove(element)            arr1.remove(element)