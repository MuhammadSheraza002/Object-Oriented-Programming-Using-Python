def square_root(n,i=0):
    if i*i*i==n:
        return i
    return square_root(n,i=i+1)

def lcm(a,b,i=1):
    maxi = max(a,b)
    if i < maxi:
        i = maxi
    if i % a == 0 and i % b == 0:
        return i
    return lcm(a,b,i+1)
import random
def main():
    print(square_root(125))
    print(lcm(8,12))

main()
