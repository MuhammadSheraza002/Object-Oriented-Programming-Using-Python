class Employee:
    def __int__(self,name,number):
        self.name = name
        self.number = number

    def __str__(self):
        return f'Name: {self.name}\tNumber: {self.number}'