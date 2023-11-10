from Objectives import *
from Subjectives import *
from mcq import *
from fill_in_the_blanks import *
from crossmatch *
from shortquestions import *
from LongQuestions import *
from Questions import *


class Exam:
    def __init__(self,title):
        self.title =title
        self.mcqs = []
        self.fill_in_blanks = []
        self.short_questions = []
        self.long_questions = []
        self.count_mcqs = int(input('Enter count of mcqs count questions (1-6): '))
        self.count_blanks = int(input('Enter count of fill in the blanks count questions (1-6): '))
        self.count_short = int(input('Enter count of short questions count questions (1-6): '))
        self.count_long = int(input('Enter count of long questions count questions (1-6): '))
        for i in range(self.count_mcqs):
            f = open
        for i in range(self.count_blanks):
        for i in range(self.count_short):
        for i in range(self.count_long):

