"""
Problem: Object Attributes
URL: https://neetcode.io/problems/python-object-attributes/question
Language: python

Solution by NeetCode GitHub Pusher
"""

class Pet:class Pet:
    def __init__(self, name: str, species: str, hunger: int, energy: int):    def __init__(self, name: str, species: str, hunger: int, energy: int):
        self.name = name        self.name = name
        self.species = species        self.species = species
        self.hunger = hunger        self.hunger = hunger
        self.energy = energy        self.energy = energy

whiskers = Pet("Whiskers", "cat", 6, 8)whiskers = Pet("Whiskers", "cat", 6, 8)
