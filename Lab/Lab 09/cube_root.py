def cube_root(number,i=0):
    if i == number:
        return True

    if i * i * i == number:
        return i

    cube_root(number,i=i+1)

from random import randint
def main():
    print(cube_root(1))
main()

