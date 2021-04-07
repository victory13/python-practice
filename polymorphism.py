class rectangle():
    def __init__(self,l,b):
        self.l = l
        self.b = b

    def area(self):
        print(self.l*self.b)
    def perimeter(self):
        print(2*(self.l+ self.b),"perimeter ")

class square():
    def __init__(self,side):
        self.side = side

    def area(self):
        print(self.side**2)
    def perimeter(self):
        print(self.side**4,"perimeter")

rec = rectangle(10,20)
sq = square(10)

for i in (rec,sq):
    i.area()
    i.perimeter()
