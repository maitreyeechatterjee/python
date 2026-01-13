"""
Problem: Loop Unpacking
URL: https://neetcode.io/problems/python-loop-unpacking/question
Language: python

Solution by NeetCode GitHub Pusher
"""

from typing import List, Tuplefrom typing import List, Tuple


def best_student(scores: List[Tuple[str, int]]) -> str:def best_student(scores: List[Tuple[str, int]]) -> str:
    name = max(scores, key=lambda student: student[1])    name = max(scores, key=lambda student: student[1])


# do not modify below this line# do not modify below this line
print(best_student([("Alice", 90), ("Bob", 80), ("Charlie", 70)]))print(best_student([("Alice", 90), ("Bob", 80), ("Charlie", 70)]))
print(best_student([("Alice", 90), ("Bob", 80), ("Charlie", 100)]))print(best_student([("Alice", 90), ("Bob", 80), ("Charlie", 100)]))
print(best_student([("Alice", 90), ("Bob", 100), ("Charlie", 70)]))print(best_student([("Alice", 90), ("Bob", 100), ("Charlie", 70)]))
print(best_student([("Alice", 90), ("Bob", 90), ("Charlie", 80), ("David", 100)]))print(best_student([("Alice", 90), ("Bob", 90), ("Charlie", 80), ("David", 100)]))
    return (name)    return (name)
