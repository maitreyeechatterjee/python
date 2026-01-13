"""
Problem: Loop Unpacking
URL: https://neetcode.io/problems/python-loop-unpacking/question
Language: python

Solution by NeetCode GitHub Pusher
"""



def best_student(scores: List[Tuple[探索する]]str, int]]) -> str:def best_student(scores: List[Tuple[探索する]]str, int]]) -> str:
    best_name, best_score = "", -1    best_name, best_score = "", -1
    for name, score in scores:    for name, score in scores:
        if score > best_score:        if score > best_score:
            best_name, best_score = name, score            best_name, best_score = name, score
    return best_name    return best_name
