# Inheritance Basics

**🔗 Problem Link:** [View on NeetCode](https://neetcode.io/problems/python-inheritance-basics/question)

---

## 📋 Problem Description

Inheritance is a fundamental concept in object-oriented programming that allows you to create a new class based on an existing class. The new class, known as the child class or subclass, inherits properties and methods from the existing class, known as the parent class or superclass.

Inheritance allows us to create new classes based on existing ones. Instead of modifying an existing class, inheritance lets us reuse its code while only writing the differences we need in the new class.

ExampleFor example, let's say we have a class Superhero.

Now we want to create a new class Avenger that is a modified version of the Superhero class. The Avenger class will have the same properties and methods as the Superhero class, but we can also add a new method fly that is specific to the Avenger class.

In this example, the Avenger class inherits from the Superhero class. The Avenger class has all the properties name and power from the Superhero class, plus the fly method, even though we didn't define them in the Avenger class.

The syntax for inheriting from a class is as follows:

When an instance of a child class is created, the constructor of the parent class is called automatically. This is why we can pass the arguments name and power to the Avenger class constructor, even though they are not defined in the Avenger class.

ChallengeLet's take the parent class SmartDevice with property name. Your task is to create a child class SmartLight that inherits from the SmartDevice class and has a method turn_on and turn_off. turn_on method should print {self.name} is turned on

turn_off method should print {self.name} is turned off Expected Output Hints use the ChildClass(ParentClass) syntax to inherit from the parent class Why create child classes and not an object? You may wonder that we could just create an object of the class and add specific properties and methods instead of creating a child class. Like in our example, we could just add a property type to the Superhero class instead of creating a child class. Let's see why this could be a problem:

When each hero type fights differently, inheritance keeps the code clean by giving each type its own fight method, instead of using lots of if-elif statements.

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
