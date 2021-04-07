class student:
    def __init__(self,dog):
        self.dog = dog
        print("Main method")

    def method1(self,name,age):
       #self.name_1 = name
        print(name+ " - ")
        print(age)

    def method2(self):
        # self.name_1 = name
        self.method1("ABC method 2",10)

obj1 = student("Lab")
obj2 = student("Husky")

obj1.method1("A obj1",12)
obj2.method1("B obj2",14)

obj1.method2()

#print(obj1.name_1)