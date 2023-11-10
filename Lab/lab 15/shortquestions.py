from Subjectives import *
class ShortQuestions(Subjectives):
    def __init__(self,file):
        super.__init__(file)
        f = open(file,'r')


    def __str__(self):
        return super().__str__() + '__________________________________________\n__________________________________________'



