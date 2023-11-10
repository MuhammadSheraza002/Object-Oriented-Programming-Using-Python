import copy
import Set1
import random as r

def main():
    s1 = Set1.Set()
    for i in range(20):
        s1.add_element(r.randint(10,99))
    print(s1)
    s2 = copy.deepcopy(s1)
    s2.add_element(r.randint(10,99))
    s2.add_element(r.randint(10,99))
    s2.add_element(r.randint(10,99))
    print(s1)
    print(s2)


main()
