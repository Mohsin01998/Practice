class Employee:
    increment = 1.5
    no_of_Employees = 0
    def __init__(self, fname, lname, salary):
        self.fname= fname
        self.lname= lname
        self.salary=  salary
        Employee.no_of_Employees +=1
        # self.increment = 1.4

    def increase(self):
         self.salary=int (self.salary * self.increment)

    @classmethod
    def change_increment(cls,amount):
        cls.increment = amount

    @classmethod
    def from_str(cls, emp_string):
        fname, lname, salary = emp_string.split("-")
        return cls(fname, lname, salary)

    @staticmethod
    def isopen(day):
        if day == 'sunday':
            return False
        else:
            return True
        
class Programmer(Employee):
    def __init__(self, fname, lname, salary, proglang, exp):
        super().__init__(fname, lname, salary)
        self.proglang = proglang
        self.exp = exp

    def increase(self):
         self.salary=int (self.salary * (self.increment+0.2))
         return self.salary


harry = Programmer('harry','jackson',90000, 'python', '5 years')
harry.increase()
print(harry.salary)

# mohsin = Employee('mohsin', 'hanif', 5000)
# print(Employee.isopen('monday'))

# harry = Employee ('harry', 'jackson', 42000)  

# lavish = Employee.from_str('lavish-jackson-7200')

# rohan = Employee ('rohan','hackson', 72000)


# print(lavish.fname)

# print(harry.salary)
# Employee.change_increment(5)
# harry.increase()
# print(harry.salary)

