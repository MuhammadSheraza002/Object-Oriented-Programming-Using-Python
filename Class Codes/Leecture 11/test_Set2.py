import copy
import Set2
import random as r

def main():
    s1 = Set2.Set()
    for i in range(20):
        s1.add_element(r.randint(10,99))
    print(s1)
    s2 = Set2.Set()
    for i in range(20):
        s2.add_element(r.randint(10,99))
    print(s2)
    s3 = s1 + s2
    print(s3)
    print(s1-s2)
    elements=s1.get_list()
    print(elements)


main()
