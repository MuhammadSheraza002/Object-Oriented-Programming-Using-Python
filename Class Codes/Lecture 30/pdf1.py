from fpdf import FPDF

pdf = FPDF()
pdf.add_page()

pdf.set_font("times", size = 16)
for i in range(1,5):
    pdf.cell(100,10,txt=f'this is line {i}',ln=1,align='C')
pdf.cell(100, 10, txt = "My PDF File", ln = 2, align = 'L')
pdf.set_font("times", size = 14)
pdf.cell(50, 10, txt = "This is line 1.", ln = 1, align = 'L')
pdf.cell(100, 10, txt = "This is line 2.", ln = 1, align = 'L')
pdf.cell(100, 10,txt = "This is line 3.", ln = 1, align = 'C')
pdf.cell(100, 10, txt = "This is end of document.", ln = 1, align = 'L')

pdf.output('test.pdf')
