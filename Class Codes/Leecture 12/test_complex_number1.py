import complexnumber1 as cn

def main():
    c1 = cn.Complex_Number(2,-3)
    print(f'C1: {c1}')
    c2 = cn.Complex_Number(3,4)
    print(f'C2: {c2}')
    c3 = cn.Complex_Number(3,0)
    print(f'C3: {c3}')
    c4 = cn.Complex_Number(0,-5)
    print(f'C4: {c4}')
    print(cn.Complex_Number.get_count())    #calling class level member function with class name

main()
