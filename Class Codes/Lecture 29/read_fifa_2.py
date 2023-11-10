from team import *

file = open('fifa.csv', 'r')
heading = file.readline()
teams = []
for i in range(32):
    string = file.readline().strip()
    teams.append(Team(string))
for team in teams:
    print(team)
