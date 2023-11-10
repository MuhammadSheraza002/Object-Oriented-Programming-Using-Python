from abc import *
class Question(ABC):
    q_no = 1
    def __init__(self, file, marks=1):
        self.q_no= Question.q_no
        Question.q_no += 1
        self.description = file.readline().strip()
        self.marks = marks

    @abstractmethod
    def __str__(self):
        return f'{self.q_no}.  {self.description}\t(Marks: {self.marks})'