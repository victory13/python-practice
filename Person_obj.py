class Car:
   def __init__(self,model,color,door):
        self.type_of_car = model
        self.color = color
        self.door = door


   def definer(self):
        if self.door == 2:
            print(self.type_of_car," is nahhh")

        else :
            print(self.type_of_car," is normal")