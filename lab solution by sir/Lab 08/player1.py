class Player:
    count=0
    countries=set()
    total_runs=0
    total_hundreds=0
    total_fifties=0
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
        Player.count += 1
        Player.countries.add(self.country)
        Player.total_runs += self.runs
        Player.total_hundreds += self.hundereds
        Player.total_fifties += self.fifties

    def __str__(self):
        return f'{self.name:15}\t{self.country:15}\t{self.start}-{self.end}\t{self.matches}\t{self.innings}\t{self.notout}\t{self.runs}\t{self.highest}\t{self.average}\t{self.hundereds}\t{self.fifties}\t{self.zeros}'

    def get_total_runs():
        return Player.total_runs

    def get_total_hundreds():
        return Player.total_hundreds

    def get_total_fifties():
        return Player.total_fifties

    def get_countries():
        return Player.countries
