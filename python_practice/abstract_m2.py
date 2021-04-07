from abc import ABC,abstractmethod

class Person:
    def __init__(self):
        pass

    @abstractmethod
    def breathe(self):
        print("Person is breathing")

    @abstractmethod
    def eat(self):
        print("Person is eating")

    def exercise(self):
        print("Person is exercising")

class Student(Person):
    def eat(self):
        print("Student is eating")

    def breathe(self):
        print("Student is breathing")

obj = Student()
obj.breathe()
obj.eat()
obj.exercise()
