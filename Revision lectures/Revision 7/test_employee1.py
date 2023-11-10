import employee1 as emp
def main():
    emp1 = emp.Employee('Azam Ali', 'Clerk', 35000)
    print(f'{emp1}\n--------------')
    emp1.set_c_add(21, 'A', 'Bahria Town', 'Lahore', 'Pakistan')
    print(f'{emp1}\n--------------')
    emp1.set_p_add(45, 'C', 'Wapda Town', 'Lahore', 'Pakistan')
    print(f'{emp1}\n--------------')


main()
