from random import randint
import Classroom
import Instructor
class CollegeCourse:
    course_no=0
    def __init__(self,fname,lname,office_number,building_no,room_no,cr_hours):
        CollegeCourse.course_no+=1
        self.course_no = CollegeCourse.course_no
        self.instructor = Instructor.Instructor(fname,lname,office_number)
        self.classroom = Classroom.Classroom(building_no,room_no)
        self.credit_hours = cr_hours

    def __str__(self):
        return f'Course no: {self.course_no}\tInstuctor:- {str(self.instructor)}\t Class room: {self.classroom}\tCredit hours{self.credit_hours}'


def main():
    buildings = ['A','B','C']
    oop = CollegeCourse('Sir Abdul',"Mateen Sahab",randint(1,10),buildings[randint(0,2)],randint(1,50),randint(1,4))
    probability = CollegeCourse('Sir Faisal',"Bukhari Sahab",randint(1,10),buildings[randint(0,2)],randint(1,50),randint(1,4))
    print(oop)
    print(probability)

main()