import address as ad
class Employee:
    emp_count = 0
    def __init__(self, n, d, s):
        Employee.emp_count += 1
        self.__emp_no = Employee.emp_count
        self.__name = n
        self.__designation =  d
        self.__salary = s
        self.__c_add = ''
        self.__p_add = ''

    def set_c_add(self, c_h, c_b, c_t, c_cty, c_ctry):
        self.__c_add = ad.Address(c_h, c_b, c_t, c_cty, c_ctry)

    def set_p_add(self, p_h, p_b, p_t, p_cty, p_ctry):
        self.__p_add = ad.Address(p_h, p_b, p_t, p_cty, p_ctry)

    def __str__(self):
        address=''
        if self.__c_add == '':
            address = 'No Current Address'
        else:
            address = str(self.__c_add)
        if self.__p_add == '':
            address += f'\tNo Permanent Address'
        else:
            address += f'\t{str(self.__c_add)}'
        return f'Employee No: {self.__emp_no}\nName: {self.__name}\nDesignation: {self.__designation}\n'\
            f'Salary:{self.__salary}\nCurrent Address:\n{address}'

