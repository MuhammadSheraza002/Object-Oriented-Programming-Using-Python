import random as r
def main():
    month=('January','February','March','April','May','June','July','August','September','October','November','December')
    dom=(31,28,31,30,31,30,31,31,30,31,30,31)
    d = r.randint(1,31)
    m = r.randint(1, 12)
    print (f'Month: {month[m-1]}')
    print (f'Day: {d}')
    if (dom[m-1]<m):
        print (f'Invalid day')
    else:
        print (f'Valid day')

main()
