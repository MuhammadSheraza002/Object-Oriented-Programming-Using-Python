import struct
class Marks:
        q1=0
        q2=0
        q3=0
        pres=0
        a1=0
        a2=0
        sum_q1 = 0
        sum_q2 = 0
        sum_q3 = 0
        sum_pres = 0
        sum_a1 = 0
        sum_a2 = 0
        sum_a3 = 0
        students_count = 0
	def __init__(self, rollno, q1, q2, q3, pres, a1, a2):
		self.__rollno = rollno
		self.__q1 = q1
		self.__q2 = q2
		self.__q3 = q3
		self.__pres = pres
		self.__a1 = a1
		self.__a2 = a2

        Marks.students_count += 1
        Marks.sum_q1 += self.__q1
        Marks.sum_q2 += self.__q
        Marks.sum_q3 += self.__q3
        Marks.sum_a1 += self.__a1
        Marks.sum_a2 += self.__a2
                Marks.sum_pres += self.__pres
                if Marks.q1 < self.__q1:
                        Marks.q1 = self.__q1
                if Marks.q2 < self.__q2:
                        Marks.q2 = self.__q2
                if Marks.q3 < self.__q3:
                        Marks.q3 = self.__q3
                if Marks.pres < self.__pres:
                        Marks.pres = self.__pres
                if Marks.a1 < self.__a1:
                        Marks.a1 = self.__a1
                if Marks.a2 < self.__q2:
                        Marks.a2 = self.__a2
                if Marks.q3 < self.__q3:
                        Marks.a3 = self.__a3
        def get_rollno(self):
                return self.__rollno
        def get_q1(self):
                return self.__q1
        def get_q2(self):
                return self.__q2
        def get_q3(self):
                return self.__q3
        def get_a1(self):
                return self.__a1
        def get_a2(self):
                return self.__a2
        def get_pres(self):
                return self.__pres

	def __str__(self): 
		return self.__rollno + '\t' + str(self.__q1)  + '\t' + str(self.__q2)  + '\t' + str(self.__q3)  + '\t' + str(self.__pres) + '\t\t' + str(self.__a1) + '\t\t' + str(self.__a2)
        
	@staticmethod
`   def show_statistics():
        print ('\nMarks Statistics\tQuiz1\tQuiz2\tQuiz3\tPresentation\tAssignment1\tAssignment2')
        s = 'Average Marks\t'+str(round(Marks.sum_q1/Marks.students_count,2))+'\t'+str(round(Marks.sum_q2/Marks.students_count,2))+'\t'+str(round(Marks.sum_q3/Marks.students_count,2))+'\t'+str(round(Marks.sum_pres/Marks.students_count,2))+'\t\t'+str(round(Marks.sum_a1/Marks.students_count,2))+'\t\t'+str(round(Marks.sum_a2/Marks.students_count,2))
        s += '\nMax Marks\t'+str(Marks.q1)+'\t'+str(Marks.q2)+'\t'+str(Marks.q3)+'\t'+str(Marks.pres)+'\t\t'+str(Marks.a1)+'\t\t'+str(Marks.a2)
        print (s)
