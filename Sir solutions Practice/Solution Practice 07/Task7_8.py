import random as r

def init_random_list(x, count):
    for i in range(count):
        x.append(r.randint(10,99))

def count_common_elements(x, y):
    count = 0
    for element1 in x:
        for element2 in y:
            if element1 == element2:
                count += 1
    return count


def main():
    x= []
    init_random_list(x,10)
    print(x)
    y= []
    init_random_list(y,10)
    print(y)
    z= []
    init_random_list(z,10)
    print(z)
    common_count_xy = count_common_elements(x, y)
    common_count_xz = count_common_elements(x, z)
    if common_count_xy > common_count_xz:
        print ('List 1 is more closer to list 2')
    else:
        print ('List 1 is more closer to list 3')

main()
