from fpdf import FPDF
from team import *
import os

file = open('fifa.csv', 'r')
heading = file.readline()
teams = []
for i in range(32):
    string = file.readline().strip()
    teams.append(Team(string))
file.close()


pdf = FPDF()
pdf.add_page()
pdf.set_font("times", size = 16)
pdf.cell(200, 10, txt = "FIFA World Cup 2022", ln = 1, align = 'C')
pdf.set_font("times", size = 18)
pdf.cell(200, 10, txt = "Points Table", ln = 1, align = 'C')
pdf.set_font("times", size = 14)
heading_str = ''
for item in heading.split(','):
    heading_str += item + '\t'
pdf.cell(200, 10, heading_str, ln = 1, align = 'C')
pdf.set_font("times", size = 12)
for team in teams:
    pdf.cell(200, 10, str(team), ln = 1, align = 'C')
file_name = 'fifa_worldcup_2022_points_table.pdf'
if os.path.exists(file_name):
    os.remove(file_name)
pdf.output(file_name)
