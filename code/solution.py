"""
Problem: Code
URL: https://neetcode.io/problems/python-list-initialization/solution
Language: python

Solution by NeetCode GitHub Pusher
"""




    list[int]:    list[int]:
def create_list_with_value(size: int, index: int, value: int) -> List[int]:def create_list_with_value(size: int, index: int, value: int) -> List[int]:

      arr = [0] * size      arr = [0] * size
      arr[index] = value      arr[index] = value
      return arr      return arr