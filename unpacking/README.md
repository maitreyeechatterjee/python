# Unpacking

**🔗 Problem Link:** [View on NeetCode](https://neetcode.io/problems/python-unpacking/question)

---

## 📋 Problem Description

The biggest advantage of using Python for coding interviews is its simplicity and readability. In this section we will learn some of the shortcuts Python provides to make our code easy to read and write.

One of these shortcuts is unpacking. Above, we have code that calulates the slope of a line given two points.

Each point is a list of two integers.

Notice how we have two variables on the left side of the assignment operator, with a list on the right side. This is called unpacking. We know point1 and point2 are lists of size 2, so we can unpack them into two variables each. The below code accomplishes the same without unpacking but with slightly more code:

If we attempt unpacking with not enough variables on the left-side, we will get a ValueError.

Unpacking also works with tuples and sets with the same syntax.

ChallengeImplement the following functions using unpacking: sum_3_integers(triplet: List[int]) -> int that takes a list of 3 integers and returns the sum of the integers. that takes a list of 3 integers representing [width, height, depth] of a box and returns the volume of it. That's it? You may think that these small shortcuts don't make a difference. But after you master the arts of Pythonic code, you will be able to save several lines of code as opposed to a more verbose language. For example, a 30 line function in Java may only be 15 lines in Python.

---

## 💡 Solution

Check the `solution.py` file in this directory for the complete implementation.

---

## 📊 Complexity Analysis

*Add your complexity analysis here after solving*

- **Time Complexity:** O(?)
- **Space Complexity:** O(?)

---

<sub>This problem was automatically synced from NeetCode using [NeetCode GitHub Pusher](https://github.com/)</sub>
