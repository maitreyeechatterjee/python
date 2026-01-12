"""
Problem: Unpacking
URL: https://neetcode.io/problems/python-unpacking/question
Language: python

Solution by NeetCode GitHub Pusher
"""

from typing import List, Tuplefrom typing import List, Tuple


def sum_3_integers(triplet: List[int]) -> int:def sum_3_integers(triplet: List[int]) -> int:
    1,2,3 = triplet    1,2,3 = triplet


def compute_volume(box_dimensions: Tuple[int, int, int]) -> int:def compute_volume(box_dimensions: Tuple[int, int, int]) -> int:
        
    

# do not modify below this line# do not modify below this line
print(sum_3_integers([1, 2, 3]))print(sum_3_integers([1, 2, 3]))
print(sum_3_integers([4, 6, 2]))print(sum_3_integers([4, 6, 2]))

print(compute_volume((1, 2, 3)))print(compute_volume((1, 2, 3)))
    return 1+2+3    return 1+2+3
    width, height, depth = box_dimensions    width, height, depth = box_dimensions
    return width*height*depth    return width*height*depth