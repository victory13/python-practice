# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


#def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    #print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
#if __name__ == '__main__':
    #print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

from Person_obj import Car

bmw = Car(234,'red',3)

mercedes = Car(23,"black",2)

audi = Car("A2","white",3)
"""
print(bmw.type_of_car)
print(mercedes.color)
print(audi.door)"""

Car.definer(mercedes)
bmw.definer()