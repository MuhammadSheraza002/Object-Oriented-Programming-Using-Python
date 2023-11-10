from pickle import *
from team import *

file = open('fifa.bin','rb')
teams = load(file)
file.close()
for team in teams:
    print(team)

