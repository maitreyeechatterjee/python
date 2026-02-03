"""
Problem: List Clone
URL: https://neetcode.io/problems/python-list-clone/question
Language: python

Solution by NeetCode GitHub Pusher
"""

from typing import Listfrom typing import List


def remove_element(arr: List[int], element: int) -> List[int]:def remove_element(arr: List[int], element: int) -> List[int]:
    arr_list = arr.copy()    arr_list = arr.copy()
    arr_list.remove(element)    arr_list.remove(element)
    return arr_list    return arr_list

