from subjective import *

class LongQuestion(Subjective):
    def __init__(self, file):
        super().__init__(file, 5)

    def __str__(self):
        string = Subjective.__str__(self)
        for i in range(5):
            string += '_____________________________________________________\n'
        return string