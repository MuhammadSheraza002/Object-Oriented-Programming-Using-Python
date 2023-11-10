from objective import *
class MCQ(Objective):
    def __init__(self, file):
        super().__init__(file)
        self.choice1 = file.readline().strip()
        self.choice2 = file.readline().strip()
        self.choice3 = file.readline().strip()
        self.choice4 = file.readline().strip()

    def __str__(self):
        string = super().__str__()
        return  string + f'A. {self.choice1}\nB. {self.choice2}\nC. {self.choice3}\nD. {self.choice4}'+\
                f'\nEnter Your Choice: '