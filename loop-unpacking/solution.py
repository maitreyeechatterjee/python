"""
Problem: Loop Unpacking
URL: https://neetcode.io/problems/python-loop-unpacking/question
Language: python

Solution by NeetCode GitHub Pusher
"""

def best_student(scores: List[Tuple[str, int]]) -> str:def best_student(scores: List[Tuple[str, int]]) -> str:
    name = max(scores, key=lambda)    name = max(scores, key=lambda)


    return (name)    return (name)
# do not modify below this line# do not modify below this line
print(best_student([("Alice", 90), ("Bob", 80), ("Charlie", 70)]))print(best_student([("Alice", 90), ("Bob", 80), ("Charlie", 70)]))
print(best_student([("Alice", 90), ("Bob", 80), ("Charlie", 100)]))print(best_student([("Alice", 90), ("Bob", 80), ("Charlie", 100)]))
print(best_student([("Alice", 90), ("Bob", 100), ("Charlie", 70)]))print(best_student([("Alice", 90), ("Bob", 100), ("Charlie", 70)]))