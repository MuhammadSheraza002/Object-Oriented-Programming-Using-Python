class Student
    def __init__(self,string):
        self.record = string.split(',')
        self.rollno=self.record[0]
        self.