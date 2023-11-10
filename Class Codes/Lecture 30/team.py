class Team:
    def __init__(self, string):
        self.info = string.split(',')
        self.group = self.info[0]
        self.team_name = self.info[1]
        self.matches = int(self.info[2])
        self.won = int(self.info[3])
        self.draw = int(self.info[4])
        self.loss = int(self.info[5])
        self.goals_for = int(self.info[6])
        self.goals_against = int(self.info[7])
        self.goals_difference = int(self.info[8])
        self.points = int(self.info[9])

    def __str__(self):
        #f string format used to align columns
        string = self.info[0] + '\t' + f'{self.info[1]:<15}'
        for i in range(2, 10):
            string += f'{self.info[i]:>5}'#f string format used to maintain width of columns
        return string.strip()
    def get_info(self):
        string = f'{self.info[1]:<18}'
        for i in range(2, 10):
            string += f'{self.info[i]:>10}'
        return string.strip()
