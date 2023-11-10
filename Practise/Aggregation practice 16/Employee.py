import Date

class Employee:
    def __init__(self,employee_no,name, designation, day, month, year,salary):
        self.employee_no = employee_no
        self.name = name
        self.designation = designation
        self.salary = salary
        self.join_date = Date.Date()

    def __str__(self):
        return f'Employee no:- {self.employee_no}\tName: {self.name}\tDesignation: {self.designation}\tJoining Date:-{str(self.join_date)}'

from random import randint

def main():
    e1 = Employee(randint(1,4),'Sheraz','sahiwal',randint(1,30),randint(1,12),randint(40000,50000),randint(40000,50000))
    e2 = Employee(randint(1,4),'Afraz','sahiwal',randint(1,30),randint(1,12),randint(40000,50000),randint(40000,50000))
    e3 = Employee(randint(1,4),'Ayesha','sahiwal',randint(1,30),randint(1,12),randint(40000,50000),randint(40000,50000))
    print(e1)
    print(e2)
    print(e3)

main()