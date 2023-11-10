from Objectives import *
class CrossMatch(Objectives):
    def __init__(self,file, count):
        super.__init__(file,count)
        f = open(file,'r')
        self.count = count
        self.list1 = []
        self.list2 = []
        for i in range(self.count):
            a,b = f.readline().split()
            self.list1.append(a)
            self.list1.append(b)

    def __str__(self):
        ans = super().__str__() +'\n'
        for i in range(self.count):
            ans+=self.list1[i] + '\t' + self.list2[i] +'\n'
        return ans




    def __str__(self):
        return super().__str__() +'Enter your answer: '


