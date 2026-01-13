"""
Problem: Enumerate
URL: https://neetcode.io/problems/python-enumerate/question
Language: python

Solution by NeetCode GitHub Pusher
"""

def get_dist_between_sevens(nums: List[int]) -> int:def get_dist_between_sevens(nums: List[int]) -> int:
    first_index = None    first_index = None


    for index, value in enumerate(nums):    for index, value in enumerate(nums):
        if value == 7:        if value == 7:
            if first_index is None:            if first_index is None:
                first_index = index                first_index = index
            else:            else:
                return index - first_index                return index - first_index
# do not modify below this line# do not modify below this line
print(get_index_of_seven([1, 2, 3, 4, 5, 6, 7, 8, 9]))print(get_index_of_seven([1, 2, 3, 4, 5, 6, 7, 8, 9]))


    return -1    return -1

            return index            return index
        if value == 7:        if value == 7:
    for index, value in enumerate(nums):    for index, value in enumerate(nums):
def get_index_of_seven(nums: List[int]) -> int:def get_index_of_seven(nums: List[int]) -> int: