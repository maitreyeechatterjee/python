"""
Problem: Code
URL: https://neetcode.io/problems/python-resizable-list-part-2/solution
Language: python

Solution by NeetCode GitHub Pusher
"""

from typing import Listfrom typing import List


def append_elements(arr1: List[int], arr2: List[int]) -> List[int]:def append_elements(arr1: List[int], arr2: List[int]) -> List[int]:
    

def remove_elements(arr1: List[int], arr2: List[int]) -> List[int]:def remove_elements(arr1: List[int], arr2: List[int]) -> List[int]:
    List[int]:    List[int]:


# do not modify below this line# do not modify below this line
print(append_elements([1, 2, 3], [4, 5, 6]))print(append_elements([1, 2, 3], [4, 5, 6]))
print(append_elements([4, 3], [4, 5, 3]))print(append_elements([4, 3], [4, 5, 3]))

print(remove_elements([1, 2, 3, 4, 5], [2, 4, 6]))print(remove_elements([1, 2, 3, 4, 5], [2, 4, 6]))
print(remove_elements([1, 2, 3, 4, 5], [2, 3, 4, 5, 5]))print(remove_elements([1, 2, 3, 4, 5], [2, 3, 4, 5, 5]))
print(remove_elements([1, 7, 2, 3, 4, 5], [6, 7, 8, 2]))print(remove_elements([1, 7, 2, 3, 4, 5], [6, 7, 8, 2]))
    List[int]:    List[int]:
    arr1.extend(arr2)    arr1.extend(arr2)
    return arr1    return arr1
    for element in arr2:    for element in arr2:
        if element in arr1:        if element in arr1:
            arr1.remove(element)            arr1.remove(element)
            return arr1            return arr1
