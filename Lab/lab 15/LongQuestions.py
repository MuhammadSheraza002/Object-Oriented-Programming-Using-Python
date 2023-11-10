from Subjectives import *
class LongQuestions(Subjectives):
    def __init__(self,file):
        super.__init__(file,5)
        f = open(file,'r')


    def __str__(self):
        ans = ''
        for i in range(5):
            ans += '__________________________________________'
        return super().__str__() + ans 



