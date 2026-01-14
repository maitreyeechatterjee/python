"""
Problem: Inequality
URL: https://neetcode.io/problems/python-inequality/question
Language: python

Solution by NeetCode GitHub Pusher
"""


def is_arr_valid(names: List[str], max_length: int) -> bool:def is_arr_valid(names: List[str], max_length: int) -> bool:
    if 0 < len(names) <= max_length:    if 0 < len(names) <= max_length:
        return True        return True
    return False    return False
# do not modify below this line# do not modify below this line
print(is_arr_valid(["Alice", "Bob", "Charlie"], 3))print(is_arr_valid(["Alice", "Bob", "Charlie"], 3))
print(is_arr_valid(["Alice", "Bob", "Charlie"], 2))print(is_arr_valid(["Alice", "Bob", "Charlie"], 2))
print(is_arr_valid(["Alice", "Bob", "Charlie"], 0))print(is_arr_valid(["Alice", "Bob", "Charlie"], 0))