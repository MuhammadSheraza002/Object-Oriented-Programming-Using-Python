class Subject:
    def __init__(self,sessional,mid,final):
        self.sessional = sessional
        self.mid = mid
        self.final = final

    def __str__(self):
        return f'sessional: {self.sessional} mid: {self.mid} final: {self.final}'

    def __del__(self):
        print('subject deleted')

import random
class Semester:
    def __init__(self):
        self.s1 = Subject(random.randint(0,25),random.randint(0,35),random.randint(0,40))
        self.s2 = Subject(random.randint(0,25),random.randint(0,35),random.randint(0,40))
        self.s3 = Subject(random.randint(0,25),random.randint(0,35),random.randint(0,40))
        self.s4 = Subject(random.randint(0,25),random.randint(0,35),random.randint(0,40))
        self.s5 = Subject(random.randint(0,25),random.randint(0,35),random.randint(0,40))
        self.s6 = Subject(random.randint(0,25),random.randint(0,35),random.randint(0,40))

    def __str__(self):
        return str(self.s1) +str(self.s2) +str(self.s3)+str(self.s4) +str(self.s5) +str(self.s6)
    def __del__(self):
        print('class deleted')

def main():
    s1 = Semester()
    print(s1)

main()