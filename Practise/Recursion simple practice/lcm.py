def LCM(x,y,lcm,i):
    if i < x or i < y:
        return lcm

    elif i % x == 0 and i % y==0:
        if i < lcm:
            lcm = i
    return LCM(x,y,lcm,i=-1)

from random import randint
def main():
    x = randint(0,10)
    y = randint(0,10)
    print(f'x: {x}\ny: {y}')
    print(LCM(x,y,x*y,x*y))
main()