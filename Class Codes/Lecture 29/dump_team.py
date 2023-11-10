from team import *
from pickle import *

file = open('fifa.csv', 'r')
heading = file.readline()
teams = []
for i in range(32):
    string = file.readline().strip()
    teams.append(Team(string))
file.close()
file = open('fifa.bin','wb')
dump(teams, file)
file.close()
