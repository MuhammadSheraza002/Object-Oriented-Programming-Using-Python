def my_fun(arg1, **kwargs):
    print(arg1)
    for key, value in kwargs.items():
        print(f'{key}, {value}')
    print ('---------------')

#my_fun()
my_fun(25, first=1, second=2)
my_fun('test', day=21, month='November', year=2022)
