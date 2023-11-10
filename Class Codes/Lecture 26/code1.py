def my_fun(*argv):
    for arg in argv:
        print(arg, end=' ')
    print()

my_fun()
my_fun(2, 3)
my_fun('a')
my_fun('a',2, 3)
