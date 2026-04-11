# Super Function

**🔗 Problem Link:** [View on NeetCode](https://neetcode.io/problems/python-super-function/question)

---

## 📋 Problem Description

super() is a built-in function in Python that allows you to call methods from a parent class. It's a powerful tool for working with inheritance.

Why use super()?When working with inheritance, there are often situations where you want to extend rather than completely replace a parent class's behavior. For example: You might want to add extra initialization steps while keeping the parent's initialization

You may need to enhance an existing method while maintaining its core functionality

You could need to access parent class properties while adding new ones Let's see an example:

In this example, the super() function is used to call the parent_method from the ParentClass. The super() method can be visualized as an object that points to the parent class. Remember super() itself doesn't take any arguments, but it can be used to call the parent class's methods.

Syntax for super() functionChallengeGiven the code for the SuperHero class, complete the following tasks: Create an Avenger class that inherits from the SuperHero class.

Override the __init__ method to add a team property to the Avenger class. Avenger should also call the __init__ method of the SuperHero class to initialize the name and power properties.

Define the attack method in the Avenger class, which should call the attack method of the SuperHero class. Expected Output Hints Use the super().__init__(name, power) function to call the __init__ method of the SuperHero class.

Use the super().attack() function to call the attack method of the SuperHero class.

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
