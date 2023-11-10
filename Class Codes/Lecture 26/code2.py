def my_fun(arg1, *argv):
    print (arg1, end=' ')
    for arg in argv:
        print(arg, end=' ')
    print()

#my_fun()
my_fun(2, 3)
my_fun('a')
my_fun('a',2, 3)
