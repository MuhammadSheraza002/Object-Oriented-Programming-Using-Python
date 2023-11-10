from random import *
from objective import *
class CrossMatch(Objective):
    def __init__(self, file, count):
        self.list1 = []
        self.list2 = []
        self.count = count
        super().__init__(file, count)
        for i in range(count):
            self.list1.append(file.readline().strip())
            self.list2.append(file.readline().strip())

    def __str__(self):
        string = Question.__str__(self)+'\n'
        for i in range(len(self.list1)):
            index = randint(0,len(self.list1)-1)
            stmt1 = self.list1[index]
            self.list1.remove(stmt1)
            index = randint(0,len(self.list2)-1)
            stmt2 = self.list2[index]
            self.list2.remove(stmt2)
            string += stmt1 + '  *\t*\t' + stmt2 + '\n'
        return string + f'\nEnter Your Answers: '