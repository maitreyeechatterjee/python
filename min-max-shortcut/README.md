# Min Max Shortcut

**🔗 Problem Link:** [View on NeetCode](https://neetcode.io/problems/python-min-max-shortcut/question)

---

## 📋 Problem Description

You may recall Python has built-in functions to find the minimum and maximum values. We can use these functions to condense the following code:

into:

In the above code, we check if the value of transactions is less than 0. If so, we set transactions to 0, since it doesn't make sense to have a negative number of transactions.

This is a common pattern that comes up in algorithm problems. So we condense the code slightly by taking the max() of transactions and 0. We are essentially saying transactions should never be allowed to be negative.

We can also use the min() function to ensure a value doesn't exceed a certain limit:

Sometimes we can use these functions to make our code more readable and concise, especially if we already have a bunch of nested loops or conditional statements. In other cases you may prefer to keep the original if-statement. In the above examples, we used constant values 0 and 100, but we could've also used variables.

ChallengeImplement the following functions: disallow_negatives(num: int) -> int that takes an integer and returns the integer if it is greater than or equal to 0. Otherwise, it should return 0. max_difference(nums: List[int]) -> int that takes a list of integers and returns the maximum difference between any two adjacent elements in the list, by subtracting the element on the right from the element on the left. In other words, it should return the maximum value of nums[i] - nums[i - 1] for all valid indices i. You may assume the output will always be a positive integer.

Example: Given the list [10, 1, 3, 7], the maximum adjacent difference is 7 - 3 = 4.

You may assume all input lists will have at least two elements.

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
