from enum import Enum
from collections import deque

class Animal:
    def __init__(self, name, order):
        self.name = name
        self.order = order

    def is_older_than(self, animal_b):
        return self.order < animal_b.order

class Dog(Animal):
    def __init__(self, name, order):
        super(name, order)
    
class Cat(Animal):
    def __init__(self, name, order):
        super(name, order)
  
class AnimalShelter:
    def __init__(self):
        self.dogs = deque()
        self.cats = deque()
        self.order = 0
    
    def enqueue(self, animal):
        animal.order = self.order
        self.order += 1
        if type(animal) is Dog:
            self.dogs.append(animal)
        else:
            self.cats.append(animal)

    def dequeue_dog(self):
        if len(self.animals):
            return self.dogs.popleft()
        return None
    
    def dequeue_cat(self):
        if len(self.animals):
            return self.cats.popleft()
        return None

    def dequeue_any(self):
        if len(self.dogs) == 0:
            return self.dequeue_cat()
        else if len(self.cats) == 0:
            return self.dequeue_dog()
        if self.dogs[0].is_older_than(self.cats[0]):
            return self.dequeue_dog()
        return self.dequeue_cat()



    