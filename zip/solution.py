"""
Problem: Zip
URL: https://neetcode.io/problems/python-zip/question
Language: python

Solution by NeetCode GitHub Pusher
"""

from typing import List, Dictfrom typing import List, Dict


def group_names_and_scores(names: List[str], scores: List[int]) -> Dict[str, int]:def group_names_and_scores(names: List[str], scores: List[int]) -> Dict[str, int]:

# do not modify below this line# do not modify below this line
print(group_names_and_scores(["Alice", "Bob", "Charlie"], [90, 80, 70]))print(group_names_and_scores(["Alice", "Bob", "Charlie"], [90, 80, 70]))
print(group_names_and_scores(["Jane", "Carol", "Charlie"], [25, 100, 60]))print(group_names_and_scores(["Jane", "Carol", "Charlie"], [25, 100, 60]))
print(group_names_and_scores(["Doug", "Bob", "Tommy"], [80, 90, 100]))print(group_names_and_scores(["Doug", "Bob", "Tommy"], [80, 90, 100]))
    result = {}    result = {}
    for name, score in zip(names, scores):    for name, score in zip(names, scores):
        result[name] = score        result[name] = score
    return result    return result
