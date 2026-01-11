# Sort Lambda

**🔗 Problem Link:** [View on NeetCode](https://neetcode.io/problems/python-sort-lambda/question)

---

## 📋 Problem Description

Defining a separate function just to pass it into the key parameter of the .sort() method can be cumbersome. We can use a lambda function to define a function in a single line and pass it directly to the .sort() method.

To sort a list of words by their length, we can use a lambda function like this:

The lambda function lambda word: len(word) is equivalent to the function get_word_length we defined in the previous example. It takes a word as input and returns the length of the word.

The syntax includes: The keyword lambda.

The input variable word. We can use any variable name here.

The colon :, after which we define the function body.

The expression len(word), which is the return value of the function. A lambda function must be a single expression, and it cannot contain multiple statements. It's a convenient way to define simple functions without the need to define a separate function.

ChallengeImplement the following functions: sort_words(words: List[str]) -> List[str] - This function accepts a list of words and returns a new list of words sorted based on their length, in descending order. Use a lambda function to sort the words by their length.

sort_numbers(numbers: List[int]) -> List[int] - This function accepts a list of numbers and returns a new list of numbers sorted based on their absolute value, in ascending order. Use a lambda function to sort the numbers by their absolute value.

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
