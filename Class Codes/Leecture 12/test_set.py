import random as r
def main():
    set={r.randint(1,50) for i in range(30)}
    print (set)
    print('You may count elements to verify, whether set has 30 elements or lesser')

main()
