def my_decorator_func(any_func):
    def another_fun(*args, **kwargs):
        print('******* ', end='')
        any_func(*args, **kwargs)
        print('*******')
    return another_fun

@my_decorator_func
def cube(x):
    print (x*x*x, end=' ')

@my_decorator_func
def area(width, length):
    print (f'Area: {width * length}', end=' ')

@my_decorator_func
def rectange_area(**kwargs):
    width = kwargs['side1']
    length = kwargs['side2']
    print (f'Area: {width * length}', end=' ')

cube(4)
area(5, 7)
rectange_area(side1=5, side2=8)
rectange_area(side2=5, side1=9)
