"""
Problem: Enumerate
URL: https://neetcode.io/problems/python-enumerate/question
Language: python

Solution by NeetCode GitHub Pusher
"""

def get_index_of_seven(nums: List[int]) -> int:def get_index_of_seven(nums: List[int]) -> int:
    for index, value in enumerate(nums):    for index, value in enumerate(nums):


def get_dist_between_sevens(nums: List[int]) -> int:def get_dist_between_sevens(nums: List[int]) -> int:
    first_index = None    first_index = None


# do not modify below this line# do not modify below this line
        if value == 7:        if value == 7:
            return index            return index

    return -1    return -1
    for index, value in enumerate(nums):    for index, value in enumerate(nums):
        if value == 7:        if value == 7:
            if first_index is None:            if first_index is None:

            else:            else:
                return index = first_index                return index = first_index