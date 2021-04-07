class Dog:
    def sound(self):
        print("Barking")

class Cat:
    def sound(self):
        print('Meow')

def make_sound(animal_type):
    animal_type.sound()

german_s = Dog()
persian_c = Cat()

make_sound(german_s)
make_sound(persian_c)