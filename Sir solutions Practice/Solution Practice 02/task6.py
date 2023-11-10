import random

def main():
    n = random.randint(3,6)
    k = 1
    line_break_count = 0
    line = 1
    sum = 0
    while line <= n:
        print (k, end=' ')
        line_break_count += 1
        sum += k
        if line == line_break_count:
            print(f' = {sum}')     #move to next line
            line_break_count = 0
            sum = 0
            line += 1
        else:
            print (' + ', end='')
        k = k + 1

main()
