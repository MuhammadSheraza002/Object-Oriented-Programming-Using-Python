import student as s
import random as r

def print_menu():
    print(f'\n1. Add new student\n2. Modify result\n3. Delete student')
    print(f'4. Show student\n5. Show all students\n6. Quit from system')

def add_student(students):
    rollno = input('Roll No: ')
    if rollno in students:
        print ('Student already exists')
    else:
        students[rollno] = s.Student(rollno)
        print ('Student successfully added')

def modify_student(students):
    rollno = input('Roll No: ')
    if rollno not in students:
        print ('Student does not exist')
    else:
        mid = r.randint(0, 35)
        sessional = r.randint(0, 25)
        final = r.randint(0, 40)
        students[rollno].set_mid(mid)
        students[rollno].set_sessional(sessional)
        students[rollno].set_final(final)
        print ('Record Modified')

def delete_student(students):
    rollno = input('Roll No: ')
    if rollno not in students:
        print ('Student does not exist')
    else:
        students.pop(rollno)
        print ('Student successfully deleted')

def show_student(students):
    rollno = input('Roll No: ')
    if rollno not in students:
        print ('Student does not exist')
    else:
        print(students[rollno])


def show_all_students(students):
    keys = students.keys()
    for key in keys:
        print (students[key])
