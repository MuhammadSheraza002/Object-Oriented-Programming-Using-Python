from fpdf import FPDF
import os
file = open('Englishresults.csv','r')
file.readline()
for i in range(47):
    result = file.readline().split(',')
    rollno = result[1]
    name = result[2]
    mid = result[3]
    final = result[4]
    sessional = result[5]
    total = result[6]
    grade = result[7]
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font('times', size=14)
    pdf.cell(200, 10, txt='Object Orientd Programming', ln=1, align='C')
    pdf.cell(200, 10, txt=f'{rollno}', ln=1, align='C')
    pdf.cell(200, 10, txt=f'{name}', ln=1, align='C')
    pdf.cell(200, 10, txt='Result Card', ln=1, align='C')
    pdf.cell(100, 10, txt='mid', ln=0, align='C')
    pdf.cell(100, 10, txt=f'{mid}', ln=1, align='C')
    pdf.cell(100, 10, txt='final', ln=0, align='C')
    pdf.cell(100, 10, txt=f'{final}', ln=1, align='C')
    pdf.cell(100, 10, txt='sessional', ln=0, align='C')
    pdf.cell(100, 10, txt=f'{sessional}', ln=1, align='C')
    pdf.cell(200, 10, txt='-' * 100, ln=1, align='C')
    pdf.cell(100, 10, txt=f'total\t{total}\tgrade\t{grade}', ln=0, align='C')
    pdf.output()
    '''if os.path.exists(f'{rollno}.pdf'):
        os.remove(f'{rollno}.pdf')'''


