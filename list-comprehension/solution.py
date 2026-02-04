"""
Problem: List Comprehension
URL: https://neetcode.io/problems/python-list-comprehension/question
Language: python

Solution by NeetCode GitHub Pusher
"""

from typing import Listfrom typing import List


def create_list_of_odds(n: int) -> List[int]:def create_list_of_odds(n: int) -> List[int]:
    return  [i for i in range(1,n+1,2)]    return  [i for i in range(1,n+1,2)]
        


# do not modify below this line# do not modify below this line
print(create_list_of_odds(1))print(create_list_of_odds(1))
print(create_list_of_odds(5))print(create_list_of_odds(5))
print(create_list_of_odds(6))print(create_list_of_odds(6))
print(create_list_of_odds(10))print(create_list_of_odds(10))
