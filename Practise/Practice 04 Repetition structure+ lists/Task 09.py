import random as r

def main(size):
    array = [i for i in range(2, 100)]
    for i in range(size):
        print('\t\t\t\t\t',i,' time ')
        no1 = r.randint(0,len(array))
        no2 = r.randint(0,len(array))
        print('n01:',array[no1],'no2: ',array[no2])
        array[no1],array[no2] = array[no2],array[no1]
        print('n01:', array[no1], 'no2: ', array[no2])

main(r.randint(1,4))


