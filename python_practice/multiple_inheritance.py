# class Employee:
#     def __init__(self):
#         print("This is employee")
#
# class Person:
#     def __init__(self):
#         print("This is Person")
#
# class Developer(Person,Employee):
#     def __init__(self):
#         super().__init__()
#
# obj = Developer()

class A:
    a = 'Hello'

    def contact_details(self):
        print('Contact us at ', self.a)


class B(A):
    a = 'Hey'

    def contact_details(self):
        print('Contact us at 1', self.a)


class Apple(B):
    manufacturer = 'Apple Inc'
    contact_website = 'www.apple.com/contact'
    name = 'Apple'

    def contact_details(self):
        print('Contact us at 2', self.contact_website)


class C(Apple):
    manufacturer = 'Apple Inc'

    def contact_details(self):
        print('Contact us at 3', self.manufacturer)


class MacBook(C,Apple):
    def _init_(self):
        self.year_of_manufacture = 2018


    #def contact_details(self):
    #    self.year_of_manufacture = 2018
    #    print('This MacBook was manufactured',self.year_of_manufacture)

op = MacBook()
op.contact_details()
