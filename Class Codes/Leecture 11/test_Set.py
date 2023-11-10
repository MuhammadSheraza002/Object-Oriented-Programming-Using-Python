import Set
import random as r

def main():
    s1 = Set.Set()
    for i in range(20):
        s1.add_element(r.randint(10,99))
    print(s1)
    s2 = s1
    s2.add_element(r.randint(10, 99))
    print (s1)
    print(id(s1))
    print(id(s2))

main()
