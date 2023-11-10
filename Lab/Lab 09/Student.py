from random import randint

class Student:
    student_count = 0
    def __init__(self,roll_no,mid):
        Student.student_count=+1
        self.student_count = Student.student_count
        self.__rollno = roll_no
        self.__mid = mid
        self.__final = 40 * self.__get_probabiltic_percentage(mid) / 100
        self.__sessional = 25 * self.__get_probabiltic_percentage(mid) / 100
        self.__total = self.__mid + self.__final + self.__sessional

    def __get_probabiltic_percentage(self,mid):
        percentage = int((mid * 100) / 35)
        number = randint(0,10)
        if number <= 8 and number >= 2:
            return randint(percentage//2,(100 - percentage//2))
        else:
            return randint(0,100)

    def __str__(self):
        return f'{self.__rollno}\t{self.__mid}\t{self.__final}\t{self.__sessional}\t{self.__total}'

    def get_total(self):
        return self.__rollno + self.__mid + self.__final + self.__sessional

    def get_mid(self):
        return self.__mid

    def get_final(self):
        return self.__final

    def get_sessional(self):
        return self.__sessional
