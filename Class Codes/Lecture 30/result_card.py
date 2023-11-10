from fpdf import FPDF
pdf =  FPDF()
pdf.add_page()
pdf.set_font('Arial',size=14)
pdf.cell(200,10,txt='Result Card',ln=1,align='C')
file = open('DSAF21 PROB&STATS Sessionals - Sheet1.csv','r')
students = []
heading = file.readline().strip().split(',')
print(heading)
pdf.cell(200,10)
names = []
roll_no = []
marks = []
for i in range(50):
    record = file.readline().strip().split(',')
    roll_no.append(record[0])
    names.append(record[1])
    assignment1=record[2]
    assignment2 = record[2]
    assignment3 = record[2]
    if assignment1=='':
        assignment1=0

    if assignment2 == '':
        assignment1 = 0
    if assignment3=='':
        assignment1=0
