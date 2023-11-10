def fac(n):
    if n<=1:
        return 1
    return n * fac (n-1)

def main():
    print (fac(4))
    print (fac(6))

main()
