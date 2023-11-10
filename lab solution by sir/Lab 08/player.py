class Player:
    def __init__(self, name, country, start, end, matches, innings, notout, runs, highest, average, hundereds, fifties, zeros):
        self.name = name
        self.country = country
        self.start = start
        self.end = end
        self.matches = matches
        self.innings = innings
        self.notout = notout
        self.runs = runs
        self.highest = highest
        self.average = average
        self.hundereds = hundereds
        self.fifties = fifties
        self.zeros = zeros

    def __str__(self):
        return f'{self.name:15}\t{self.country:15}\t{self.start}-{self.end}\t{self.matches}\t{self.innings}\t{self.notout}\t{self.runs}\t{self.highest}\t{self.average}\t{self.hundereds}\t{self.fifties}\t{self.zeros}'
