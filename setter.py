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

    def increase(self):
         self.salary=int (self.salary * (self.increment+0.2))
         return self.salary

    @property
    def email(self):
        return self.fname +'.' +self.lname + '@email.com'

    @email.setter
    def email(self,given_email):
        name_list=given_email.split('@')[0].split('.')
        print(name_list)
        self.fname=name_list[0]
        self.lname=name_list[1]

if __name__=='__main__':
    harry = Employee ('harry', 'jackson', 42000) 
    rohan = Employee ('rohan','hackson', 72000)
    print(rohan.email,harry.email)
    rohan.lname='khana'
    print(rohan.email)
    rohan.email='khana.rohan@gmail.com'
    print(rohan.email)


