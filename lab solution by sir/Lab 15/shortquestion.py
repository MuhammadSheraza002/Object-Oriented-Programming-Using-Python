from subjective import *
class ShortQuestion(Subjective):
    def __init__(self, file):
        super().__init__(file, 2)

    def __str__(self):
        string = Question.__str__(self)
        for i in range(2):
            string += '\n-------------------------------------------'
        return string + '\n'