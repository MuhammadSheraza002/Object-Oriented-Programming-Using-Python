import complexnumber as cn

def do():   #do is just a function to check scope
    c1 = cn.Complex_Number(2,-3)
    print(f'C1: {c1}')
    c2 = cn.Complex_Number(3,4)
    print(f'C2: {c2}')
    print(f'Objects count before multiplication operation:{cn.Complex_Number.count}')
    c3 = c1 * c2
    print (f'c1 x c2 = {c3}')
    print(f'Objects count after multiplication operation:{cn.Complex_Number.count}')

def main():
    print(f'Objects Count:{cn.Complex_Number.count}')
    do()                            #function is called, count is print, before and after the function
    print(f'Objects count in main after function call:{cn.Complex_Number.count}')
    c = cn.Complex_Number(3,5)
    print(f'Objects count in main after object creation:{cn.Complex_Number.count}')
    del(c)
    print(f'Objects count in main after object deletion:{cn.Complex_Number.count}')

main()
