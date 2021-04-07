# class Employee:
#     def __init__(self,name,surname,age,salary):
#         self.name = name
#         self.surname = surname
#         self.age = age
#         self.salary = salary
#
#     def welcome(self):
#         print("Welcome ",self.name)
#
# class Developer(Employee):
#     def __init__(self,name,surname,age,salary,department):
#         super().__init__(name,surname,age,salary)
#         self.department =department
#
# class Manager(Employee):
#     pass
#
# emp = Developer('Jim','Pitt',25,1000,"Data")
# print(emp.name)

#  multilevel Inheritance
class A:
    def __init__(self):
        print("init function of A")

class B(A):
    def __init__(self):
        super().__init__()
        print("init function B")
class C(B):
    def __init__(self):
        super().__init__()
        print("init function C")

obj1 = C()
