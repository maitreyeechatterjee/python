# Resizable List Part 1

**🔗 Problem Link:** [View on NeetCode](https://neetcode.io/problems/python-resizable-list-part-1/question)

---

## 📋 Problem Description

Some languages have both fixed-size arrays and resizable arrays. In Python, we only have resizable arrays, which are referred to as lists in Python. This means that we can add or remove elements from a list at any time.

The common operations on a list include: append(): Adds an element to the end of the list.

pop(): Removes and returns the last element of the list.

If the list is already empty, we will get an IndexError.

We can also pass an integer to pop() to remove an element at a specific index.

If we pop(index) an index that is out of bounds, we will get an IndexError. insert(): Inserts an element at a specified index in the list.

If the index is too large, the element will be inserted at the end of the list.

If the index is negative, the element will be inserted at the beginning of the list. Here are examples of each:

ChallengeImplement the following functions: . It should append the elements of arr2 to the end of arr1 and return the resulting list.

pop_n(arr: List[int], n: int) -> List[int]. It should remove the last n elements from the list and return the resulting list. If n is greater than the length of the list, it should return an empty list.

. It should insert the element at the specified index in the list and return the resulting list. If the index is out of bounds, you should insert it at the end of the list. Time Complexity

append()

Time complexity: O(1)O(1)O(1) pop().

Time complexity: O(1)O(1)O(1) insert().

Time complexity: O(n)O(n)O(n), where nnn is the number of elements in the list.

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
