import random as r

class Set:
    def __init__(self):
        self.__elements = []

    def element_not_exist(self, element):
        for e in self.__elements:
            if e == element:
                return False
        return True

    def add_element(self, element):
        if self.element_not_exist(element):
            self.__elements.append(element)

    def __str__(self):
        s = ''
        for element in self.__elements:
            s = s + str(element) + ' '
        return s


    def is_subset(self,s):
        for i in self.__elements:
            if i not in s.__elements:
                return False
        return True

    def compare(self,s):
        same = True
        for i in self.__elements:
            if i not in s.__elements:
                same =  False
        if same:
            for i in s.__elements:
                if i not in self.__elements:
                    return False
            return True
        else:
            return False

    def elements_not_in_set2(self,set):
        count = 0
        for i in self.__elements:
            if i not in set.__elements:
                count+=1
        return count



def main():
    s1 = Set()
    s2 = Set()
    for i in range(5):
        s1.add_element(r.randint(10,50))
    for i in range(10):
        s2.add_element(r.randint(10,50))
    print('s1: ',s1)
    print('s2: ',s2)
    if s1.is_subset(s2):
        print('s1 is subset of s2')
    else:
        print('s1 is not subset of s2')

    s3 = Set()
    s4 = Set()
    for i in range(10):
        s3.add_element(r.randint(10, 50))
    for i in range(10):
        s4.add_element(r.randint(10, 50))
    print('s3: ',s3)
    print('s4: ',s4)
    if s3.compare(s4):
        print('s3 is super set of s4')
    else:
        print('s3 is not super set of s4')
    print(s3.elements_not_in_set2(s4))

main()