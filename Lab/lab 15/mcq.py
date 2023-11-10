from Objectives import *
class MCQ(Objectives):
    def __init__(self,file):
        super.__init__(file)
        f = open(file,'r')
        self.choice1 = f.readline()
        self.choice2 = f.readline()
        self.choice3 = f.readline()
        self.choice4 = f.readline()

    def __str__(self):
        return super().__str__() + self.choice1 + self.choice2 + self.choice3 + self.choice4 + 'Enter your choice: '

