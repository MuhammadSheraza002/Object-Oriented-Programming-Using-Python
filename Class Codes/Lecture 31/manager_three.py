class Manager:
    __count = -1
    def __new__(cls, salary):
        if cls.__count >= 2:
                return None
        cls.__count += 1
        obj = super(Manager, cls).__new__(cls)
        obj.set_member(salary)
        return obj
    def set_member(self, salary):
        self.salary = salary
    def __str__(self):
        return f'Salary: {self.salary}'

m1 = Manager(60000)
m2 = Manager(65000)
if m1 == m2:
    print ('Both are same')
else:
    print ('They are different')
print(m1)
print(m2)
m3 = Manager(63000)
print(m3)
m4 = Manager(61000)
print(m4)
