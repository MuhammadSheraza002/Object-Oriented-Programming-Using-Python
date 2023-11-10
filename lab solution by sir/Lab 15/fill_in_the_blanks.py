from objective import *
class Fill_In_The_Blanks(Objective):
    def __init__(self, file):
        super().__init__(file)

    def __str__(self):
        return Question.__str__(self)+'\nWrite Your Answer: '