def my_decorator_func(any_func):
    #Here another_fun is called wrapper function, which is wrapping cube function
    def another_fun(x):
        print('******* ', end='')
        any_func(x)
        print('*******')
    return another_fun

@my_decorator_func
def cube(x):
    print (x*x*x, end=' ')

cube(4)
cube(7)
