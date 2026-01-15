# List Clone

**🔗 Problem Link:** [View on NeetCode](https://neetcode.io/problems/python-list-clone/question)

---

## 📋 Problem Description

It's common to need to make a copy of a list in many algorithms. Python provides multiple ways to clone a list. Here are a few ways to do it: Using the copy() method: Using the slicing syntax: Using the list() constructor: Keep in mind, that if you have a list of objects, the above methods will not create deep copies of the elements within the list. In this case we have a list of integers, which are primitive types, so we don't need to worry about that. But if you had a list of lists, for example, you would need to use the copy.deepcopy() method to create a deep copy. Using copy.deepcopy() for deep copies: ChallengeImplement the following function: that takes a list of integers and returns a new list with the specified element removed. You should not modify the original list.

You may assume the element is always in the list. Tip: It's okay if you don't remember how to remove an element from a list. You can look back at a previous lesson or do a quick search to refresh your memory.

Time Complexity

Time complexity: O(n)O(n)O(n) where nnn is the length of the list being copied.

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
