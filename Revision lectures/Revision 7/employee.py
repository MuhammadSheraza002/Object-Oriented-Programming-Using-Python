import address as ad
class Employee:
    emp_count = 0
    def __init__(self, n, d, s , c_h, c_b, c_t, c_cty, c_ctry, p_h, p_b, p_t, p_cty, p_ctry):
        Employee.emp_count += 1
        self.__emp_no = Employee.emp_count
        self.__name = n
        self.__designation =  d
        self.__salary = s
        self.__c_add = ad.Address(c_h, c_b, c_t, c_cty, c_ctry)
        self.__p_add = ad.Address(p_h, p_b, p_t, p_cty, p_ctry)

    def __str__(self):
        return f'Employee No: {self.__emp_no}\nName: {self.__name}\nDesignation: {self.__designation}\n'\
            f'Salary:{self.__salary}\nCurrent Address:\n{str(self.__c_add)}\nPermanent Address\n{str(self.__p_add)}'

    def get_str(self):
        return f'{self.__emp_no} {self.__name}\t{self.__designation}\t{self.__salary}\t{self.__c_add.get_str()}\t{self.__p_add.get_str()}'
