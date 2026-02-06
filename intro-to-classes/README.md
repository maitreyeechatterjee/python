# Intro to Classes

**🔗 Problem Link:** [View on NeetCode](https://neetcode.io/problems/python-intro-to-classes/question)

---

## 📋 Problem Description

Imagine you're a game developer creating a superhero game. You start by defining individual heroes:

This approach has a few problems: Repetition: You have to define each hero individually.

Messy code: It's hard to keep track of all the hero attributes and their values.

Scalability: What if you need to create 50 different heroes? Your code would become unmanageable very quickly. ClassesA class is a blueprint for creating objects. Here's the basic syntax for defining a class in Python:

In Python, a class is defined with the keyword word class followed by the name of the class and a colon. The __init__ method is a special method that belongs to the class. It creates an object and initializes it's attributes.

Notice that the __init__ method has an argument self. This is required. The self variable allows us to add attributes to our object. It also prevents name conflicts, since name and self.name are different variables.

ChallengePlease see the starter code on the right and complete the following tasks: Define a class named Pet.

Define a method for initialization: def __init__(self, name, species)

Inside the __init__ method, initialize two attributes:

self.name: assigned the value of the name parameter

self.species: assigned the value of the species parameter What is the self argument? In Python, self represents the instance of the class. It's used to access variables and methods associated with the class. When you create an object from a class, Python automatically passes the object as the first argument to the __init__ method. You can name this argument anything you like, but self is the convention. Don't worry if this doesn't make sense right now. We'll cover it in more detail in the upcoming lessons. How to name classes in Python? Class names in Python use PascalCase convention, meaning each word starts with a capital letter and there are no underscores between words (e.g., SuperHero, IronMan, SpiderMan).

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
