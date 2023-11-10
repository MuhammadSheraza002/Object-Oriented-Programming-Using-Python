from myfunctions import *

def main():
    students={}
    while True:
        print_menu()
        choice = int(input ('Enter Your Choice: '))
        if choice == 1:
            add_student(students)
        elif choice == 2:
            modify_student(students)
        elif choice == 3:
            delete_student(students)
        elif choice == 4:
            show_student(students)
        elif choice == 5:
            show_all_students(students)
        else:
            print ('Thank, for using the system')
            break

main()
'''
def main():
    students={}
    while True:
        print_menu()
        list = []

main()
'''