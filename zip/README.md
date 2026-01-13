# Zip

**🔗 Problem Link:** [View on NeetCode](https://neetcode.io/problems/python-zip/question)

---

## 📋 Problem Description

Python provides an easy way to iterate over multiple lists at the same time using the zip() function. The zip() function takes multiple lists as arguments and returns an iterator of tuples. Each tuple contains an element from each list.

This is useful when we have multiple lists of the same length and want to iterate over them together.

ChallengeImplement the following function using zip(): that takes two lists, names and scores, and returns a dictionary where the key is names[i] and it maps to scores[i] as the value. You may assume the inputs names and scores will always be the same length.

Time and Space Complexity

Time complexity: O(1)O(1)O(1)

The zip() function returns an iterator at the beginning of the input lists, so it doesn't traverse the entire lists. Space complexity: O(1)O(1)O(1)

The zip() function returns an iterator so it doesn't actually create a new list of tuples in memory.

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
