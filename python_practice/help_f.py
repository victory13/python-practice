"""
help()
issubclass()

"""
class Employee:
    def __init__(self,name,surname,salary):
        self.name = name
        self.surname =surname
        self.salary = salary

class Developer(Employee):
    language = ['Java','Python','C++','Javascript']

class Manager(Developer):
    manage_dep = 'Engineering'

obj = Manager('nini','roro',25)
#help(obj)

#print(isinstance(obj,Employee))

print(issubclass(Developer,Manager))