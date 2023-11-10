from team import *
class Tournament:
    def __init__(self, file):
        self.teams = []
        file.readline() #read heading and ignore to move pointer to first team record
        for i in range(32):
            self.teams.append(Team(file.readline().strip()))
    def __str__(self):
        string = ''
        for team in self.teams:
            string += str(team) + '\n'
        return string
