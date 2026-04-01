# Method Overriding

**🔗 Problem Link:** [View on NeetCode](https://neetcode.io/problems/python-method-overriding/question)

---

## 📋 Problem Description

So far, we have seen how to inherit properties and methods from a parent class. But what if we want to change the behavior of a method in a child class? This is where method overriding comes in.

Method overriding allows us to change the behavior of a method in a child class. This is useful when we want to change the behavior of a method that is inherited from a parent class.

Let's see an example:

In this example, we have a Superhero class with a fight method. We then have a Avenger class that inherits from the Superhero class. The Avenger class has its own fight method that overrides the fight method in the Superhero class.

Above, we create an instance of the Avenger class and call the fight method. The fight method in the Avenger class is called instead of the fight method in the Superhero class.

The method from the child class is called instead of the method from the parent class. This is method overriding.

ChallengeYou are given the code for an Animal class. Your tasks are: Create a Dog class and a Cat class that inherit from the Animal class.

Override the make_sound method in the Dog class to make the dog bark. Use the print statement print(f"{self.name} is barking").

Override the make_sound method in the Cat class to make the cat meow. Use the print statement print(f"{self.name} is meowing"). Expected Output: Hint Remember the synntax for class inheritance. Remember the synntax for method overriding.

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
