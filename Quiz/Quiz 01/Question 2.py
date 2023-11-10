import random

def sort_a_b_c_d():
    a = random.randint(10,99)
    b = random.randint(10,99)
    c = random.randint(10,99)
    d = random.randint(10,99)
    print (f'A: {a}  B: {b}  C: {c}  D: {d}')
    if a > b:
        temp = b
        b = a
        a = temp
    if b > c:
        temp = b
        b = c
        c = temp
    if c > d:
        temp = d
        d = c
        c = temp
    if a > b:
        temp = b
        b = a
        a = temp
    if b > c:
        temp = b
        b = c
        c = temp
    if a > b:
        temp = b
        b = a
        a = temp
    print (f'A: {a}  B: {b}  C: {c}  D: {d}')