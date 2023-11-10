from random import randint
import Course
import Student
import Teacher


class Course_Class_Teacher:
    def __init__(self,course_code,course_title,fname,lname):
        self.__Course = Course.Course(course_code,course_title)
        self.__teacher_name = Teacher.Teacher(fname,lname)
        self.__record = []
        for i in range(1,11):
            self.__record.append(Student.Student(i,randint(0,35)))

    def __str__(self):
        result = ''
        for i in self.__record:
            result = result + str(i) + '\n'
        return f'{str(self.__Course)}\n{self.__teacher_name}\nR_no\tMid\tFinal\tTotal\n{result}'

    def get_passed_students(self):
        result =  f'{str(self.__Course)}\n{self.__teacher_name}\nR_no\tMid\tFinal\tTotal\n'
        for i in range(0,10):
            if self.__record[i].get_total() >= 50:
                result += str(self.__record[i]) + '\n'
        return result


    '''def sort_students_descending_total_marks(self):
        result = 'R_no\tMid\tFinal\tTotal\n'
        for i in range(9, 0,-1):
            for J in range(i,i+1):
                if self.__record.[i].get_total() > 50:
                    result += str(self.__record[i]) + '\n'
        return result'''

def main():
    cct = Course_Class_Teacher('cc-221','OPerating Systems','Tahir','Ali')
    print(cct)
    print(cct.get_passed_students())

main()