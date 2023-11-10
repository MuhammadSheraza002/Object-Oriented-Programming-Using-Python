import random

def main():
    n = random.randint(5,9)
    k = 1
    line_break_count = 0
    line = 1
    while line <= n:
        print (k, end=' ')
        line_break_count += 1
        if line == line_break_count:
            print()     #move to next line
            line_break_count = 0
            line += 1
        k = k + 1

main()
