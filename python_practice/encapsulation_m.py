# Protected members
class Shape:
    _length = 40 #protected variables
    _breadth = 20

class Circle(Shape):
    def __init__(self): #printing protected variables in the derived class
        print(self._length)
        print(self._breadth)

cr = Circle()  # gives output 40 20

print(cr._length)
