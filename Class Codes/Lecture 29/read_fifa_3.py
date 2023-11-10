from team import *

file = open('fifa.csv', 'r')
heading = file.readline()
teams = []
for i in range(32):
    string = file.readline().strip()
    teams.append(Team(string))
most_difference = -99999999
most_difference_team_name = ''
for team in teams:
    if team.goals_difference > most_difference:
        most_difference_team_name = team.team_name
        most_difference = team.goals_difference
print(f'{most_difference_team_name} has most goal difference, which is: {most_difference}')
