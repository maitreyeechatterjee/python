# Resizable List Part 2

**🔗 Problem Link:** [View on NeetCode](https://neetcode.io/problems/python-resizable-list-part-2/question)

---

## 📋 Problem Description

These list operations are less common, but they are absolutely worth knowing: index(): Returns the index of the first occurrence of a specified element in the list.

If the element is not in the list, we will get an ValueError. remove(): Removes the first occurrence of a specified element from the list.

extend(): Adds the elements of another list to the end of the list. Here are examples of each:

If we want to check if an element is in a list, we can use the in operator:

This is preferable to using index() unless we actually need the index of the element.

ChallengeImplement the following functions: . It should append the elements of arr2 to the end of arr1 and return the resulting list. Yes, this is the same function from the previous lesson.

. It should remove all elements of arr2 from arr1 and return the resulting list.

If any of the elements in arr2 are not in arr1, then skip them.

You don't have to worry about implementing an efficient solution. Try to use the built-in functions. Time Complexity

index()

Time complexity: O(n)O(n)O(n), where nnn is the length of the list. remove().

Time complexity: O(n)O(n)O(n), where nnn is the length of the list. extend().

Time complexity: O(m)O(m)O(m), where mmm is the length of the list passed to extend(). in operator on a list.

Time complexity: O(n)O(n)O(n), where nnn is the length of the list.

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
