from question import *

class Subjective(Question):
    def __init__(self, file, marks=2):
        super().__init__(file, marks)

    def __str__(self):
        return super().__str__()+' \n'