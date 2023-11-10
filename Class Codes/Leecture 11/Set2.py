import copy
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

    def __add__(self, o2):
        new_set = copy.deepcopy(self)
        for element in o2.__elements:
            if self.element_not_exist(element):
                new_set.__elements.append(element)
        return new_set

    def __sub__(self, o2):
        new_set = Set()
        for element in self.__elements:
            if o2.element_not_exist(element):
                new_set.__elements.append(element)
        return new_set

    def __str__(self):
        s = ''
        for element in self.__elements:
            s = s + str(element) + ' '
        return s

    def get_list(self):
        my_list = [element for element in self.__elements]
        return my_list
