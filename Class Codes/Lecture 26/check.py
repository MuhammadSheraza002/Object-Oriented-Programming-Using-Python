def check(argv):
    n = len(argv)
    start, stop, step=0, 10, 1
    if n == 1:    stop = argv[0]
    if n == 2:    start, stop = argv[0], argv[1]
    if n == 3:    start, stop, step = argv[0], argv[1], argv[2]
    while start < stop:
        print(start, end=' ')
        start += step
    print()

def print_counting(*args):
    check(args)

print_counting()
print_counting(5)
print_counting(3, 8)
print_counting(3, 8, 2)
