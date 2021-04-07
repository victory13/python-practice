class Company:
    year = 2021 # class variable
    def __init__(self,name,lname,salary,dept):
        self.name = name  # instance variable
        self.lname = lname
        self.salary = salary
        self.dept = dept

    def remove(self):
        print("Removed: ",self.name)

    def raise_salary(self):
        print("Salary raised by 25K for this employee: ",self.name,", New Salary: ",(int(self.salary)+ 25000))

    @classmethod
    def welcome(cls):
        print("Hey this is a class method and you can call it using class name")

    @staticmethod
    def congrats():
        print("Congratulations !! You made it this far. Keep it up !! ")

emp1 = Company("Jim","Shell",20000,"Finance")
emp2 = Company("Trisha","Miller",29000,"Engineer")

emp1.year= 1996

emp1.raise_salary()
emp2.raise_salary()
print(Company.year, "new company year")
print(emp1.year, "employee year")

Company.welcome()  #same as emp1.welcome()
Company.congrats() # same as emp1.congrats()
