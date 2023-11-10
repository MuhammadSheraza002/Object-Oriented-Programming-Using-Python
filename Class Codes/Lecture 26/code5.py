def my_fun(*args, **kwargs):
    print(kwargs)
    for arg in args:
        print(arg, end=' ')
    print ()
    for key, value in kwargs.items():
        print(f'{key}, {value}', end=' ')
    print ('\n---------------')

#my_fun()
my_fun(25, first=1, second=2)
my_fun('test', 36, 45, day=21, month='November', year=2022)