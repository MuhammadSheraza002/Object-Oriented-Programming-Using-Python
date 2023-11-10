class Instructor:
    def __init__(self,fname,lname,office_number):
        self.fname = fname
        self.lname = lname
        self.office_number=office_number

    def __str__(self):
        return f'first name: {self.fname}\tlast name: {self.lname}\toffice_number: {self.office_number}'
