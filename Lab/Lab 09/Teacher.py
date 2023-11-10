class Teacher:
    def __init__(self,fname,lname):
        self.__fname = fname
        self.__lname = lname

    def __str__(self):
        return f'Teacher: {self.__fname} {self.__lname}'