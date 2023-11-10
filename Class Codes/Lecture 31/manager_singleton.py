class Manager:
    manager = None
    def __new__(cls, salary):
        if Manager.manager == None:
            cls.manager = super(Manager, cls).__new__(cls)
            cls.manager.set_member(salary)
        return cls.manager
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

class abc:
    def __new__(cls,name):
        cls.abc = super(abc,cls).__new__(cls,name)
        cls.abc.set_name(name)
        return cls.abc