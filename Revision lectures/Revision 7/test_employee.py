import employee as emp
def main():
    emp1 = emp.Employee('Azam Ali', 'Clerk', 35000, 21, 'A', 'Bahria Town', 'Lahore', 'Pakistan',\
            45, 'C', 'Wapda Town', 'Lahore', 'Pakistan')
    emp2 = emp.Employee('Babar Khan', 'Cashier', 40000, 32, 'B', 'Sunny Town', 'Lahore', 'Pakistan',\
            56, 'E', 'Ali Town', 'Lahore', 'Pakistan')
    emp3 = emp.Employee('Wajid Munir', 'Clerk', 38000, 12, 'D', 'Bahria Town', 'Lahore', 'Pakistan',\
            51, 'F', 'Township', 'Lahore', 'Pakistan')
    emp4 = emp.Employee('Rafeeq Butt', 'Peon', 18000, 38, 'B', 'Green Town', 'Lahore', 'Pakistan',\
            45, 'F', 'Wapda Town', 'Sahiwal', 'Pakistan')
    print(emp1)
    print(emp1.get_str())
    print(emp2.get_str())
    print(emp3.get_str())
    print(emp4.get_str())


main()
