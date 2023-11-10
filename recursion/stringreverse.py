def main(s,n=0):
    if n == 0:
        print(s[n])
        return
    print(s[n],end='')
    main(s,n-1)
main('cba',2)

