from abc import ABC,abstractmethod

class Question(ABC):
    question_no = 0

    def __init__(self,file,marks=0):
        f = open(file,'r')
        self.discription =  f.read()
        Question.question_no+=1
        self.question_no = Question.question_no
        self.marks = marks

    @abstractmethod
    def __str__(self):
        return f'{self.question_no}.{self.discription}\t({self.marks})'
