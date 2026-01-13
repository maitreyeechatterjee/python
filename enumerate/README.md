# Enumerate

**🔗 Problem Link:** [View on NeetCode](https://neetcode.io/problems/python-enumerate/question)

---

## 📋 Problem Description

Suppose we wanted to loop over an array and we needed to access both the index and the element at that index. This is simple to accomplish:

But the Pythonic way to do this is to use the enumerate() function:

The enumerate() function returns a tuple of the index and the element at that index. We can unpack this tuple into two variables in the for loop.

The main benefit of this approach is the readability improvement, especially if we use good variable names. This allows us to easily write self-documenting code, just like when we use for in loops as shown below.

ChallengeImplement the following functions using enumerate(): get_index_of_seven(nums: List[int]) -> int that returns the index of the first occurrence of the number 7 in the list nums, or -1 if 7 is not found.

get_dist_between_sevens(nums: List[int]) -> int that returns the distance between the first and second occurrence of the number 7 in the list nums.

You may assume that there will always be at least two occurrences of the number 7 in the list.

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
