import struct
import marks

def main():
     m1 = marks.Marks('R1', 9.5, 8.5, 6.75, 90, 45, 70)
     m2 = marks.Marks('R2', 8.5, 9.5, 9.00, 80, 40, 75)
     m3 = marks.Marks('R3', 7.0, 9.0, 8.75, 85, 42, 80)
     print('Roll no\tQuiz1\tQuiz2\tQuiz3\tPresentation\tAssignment1\tAssignment2')
     print(m1)
     print(m2)
     print(m3)
     print
     marks.Marks.show_statistics()

main()
