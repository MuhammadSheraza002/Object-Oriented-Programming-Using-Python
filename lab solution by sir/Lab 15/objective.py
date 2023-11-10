from question import *

class Objective(Question):
    def __init__(self, file, marks=1):
        super().__init__(file, marks)

    def __str__(self):
        return super().__str__()+'\n'