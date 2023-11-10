from mcq import *
from fill_in_the_blanks import *
from crossmatch import *
from shortquestion import *
from longquestion import *

class Exam:
    def __init__(self, title):
        self.title = title
        self.total_marks = 0
        self.mcqs = []
        self.fill_in_the_blanks = []
        self.crossmatch = None
        self.short_questions = []
        self.long_questions = []
        mcq_count = int(input('Enter count of MCQ questions (1-6):'))
        self.total_marks +=  mcq_count
        file = open('mcq.txt')
        for i in range(mcq_count):
            self.mcqs.append(MCQ(file))
        file.close()
        fill_in_the_blanks_count = int(input('Enter count of fill in the blanks_count questions (1-6):'))
        self.total_marks +=  fill_in_the_blanks_count
        file = open('fill_in_the_blanks.txt')
        for i in range(fill_in_the_blanks_count):
            self.fill_in_the_blanks.append(Fill_In_The_Blanks(file))
        file.close()
        cross_match_count = int(input('Enter count of statements in crossmatch qustion(1-6):'))
        if cross_match_count > 0:
            file = open('crossmatch.txt')
            self.crossmatch= CrossMatch(file, cross_match_count)
            self.total_marks += cross_match_count
        file.close()
        short_questions_count = int(input('Enter count of short questions:'))
        self.total_marks +=  short_questions_count
        file = open('short.txt')
        for i in range(short_questions_count):
            self.short_questions.append(ShortQuestion(file))
        file.close()
        long_questions_count = int(input('Enter count of long questions:'))
        self.total_marks +=  long_questions_count
        file = open('/home/mateen/Documents/Python_OOP/Lab 15/long.txt')
        for i in range(long_questions_count):
            self.long_questions.append(LongQuestion(file))
        file.close()
    def __str__(self):
        string = f'\t\tExam ABC\t\t({self.total_marks})\n'
        if len(self.mcqs) > 0:
            string += ' M C Q \n_______________\n'
            for mcq in self.mcqs:
                string += str(mcq) + '\n'
        if len(self.fill_in_the_blanks) > 0:
            string += ' Fill in the blanks\n________________________\n'
            for blank in self.fill_in_the_blanks:
                string += str(blank) + '\n'
        if self.crossmatch != None:
            string += str(self.crossmatch) + '\n'
        if len(self.short_questions) > 0:
            string += ' Short Question(s) \n____________________\n'
            for question in self.short_questions:
                string += str(question) + '\n'
        if len(self.long_questions) > 0:
            string += ' Long Question(s) \n____________________\n'
            for question in self.long_questions:
                string += str(question) + '\n'
        return string