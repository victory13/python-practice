# class first:
#     def method1(self):
#         print("method 1 from first")
#     def method2(self):
#         print("method 2 from first")
#
# class second(first):
#     def method1(self):
#         print("method 3 from second")
#     def method4(self):
#         print("method 4 from second")
#
# class third(second,first):
#     def method5(self):
#         print("method 5 from third")
#     def method6(self):
#         print("method 6 from third")
#
# sec= third()
# sec.method1()
## area

class rectangle():
    def __init__(self,l,b):
        self.length = l
        self.breadth = b
        print("rectangle init")

    def perimeter(self):
        print("Perimeter is ",2*(self.length+self.breadth))

    def area(self):
        print(self.length*self.breadth,"Area ")

class circle:
    def __init__(self,radius,radius_1):
        print("circle init")

class square(rectangle,circle):
    def __init__(self,side):
        super().__init__(side,side)
        print("square")

sq = square(5)

sq.perimeter()
sq.area()