class Stack:
    def __init__(self):
        self.__data = []
    def push(self, element):
        self.__data.append(element)
    def pop(self):
        self.__data.pop() #pop delete last index of list
    def is_empty(self):
        if len(self.__data) == 0:   return True
        return False


