def my_decorator_func(any_func):
    def another_fun(*x):
        print('******* ', end='')
        any_func(*x)
        print('*******')
    return another_fun

@my_decorator_func
def cube(x):
    print (x*x*x, end=' ')

@my_decorator_func
def area(width, length):
    print (f'Area: {width * length}', end=' ')

cube(4)
cube(7)
area(5, 7)
