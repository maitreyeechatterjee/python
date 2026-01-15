"""
Problem: Code
URL: https://neetcode.io/problems/python-resizable-list-part-2/solution
Language: python

Solution by NeetCode GitHub Pusher
"""

    

def remove_elements(arr1: List[int], arr2: List[int]) -> List[int]:def remove_elements(arr1: List[int], arr2: List[int]) -> List[int]:
    List[int]:    List[int]:
        for element in arr2:        for element in arr2:
        if element in arr1:        if element in arr1:
            arr1.remove(element)            arr1.remove(element)
        return arr1        return arr1
