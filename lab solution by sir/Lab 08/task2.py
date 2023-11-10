import player1 as p

def read_data(players):
    file = open("players.txt", 'r')
    record = file.read()
    lines = record.split('\n')
    file.close()
    for i in range(0, len(lines), 13):
        name = lines[i]
        country=lines[i+1]
        start=int(lines[i+2])
        end=int(lines[i+3])
        matches=int(lines[i+4])
        innings=int(lines[i+5])
        notout=int(lines[i+6])
        runs=int(lines[i+7])
        highest=int(lines[i+8])
        average=float(lines[i+9])
        hundereds=int(lines[i+10])
        fifties=int(lines[i+11])
        zeros=int(lines[i+12])
        players.append(p.Player(name, country, start, end, matches, innings, notout, runs, highest, average, hundereds, fifties, zeros))

def print_player_names_country_wise(players):
    countries = p.Player.get_countries()
    for country in countries:
        print (f'*******  {country} *******')
        for player in players:
            if player.country == country:
                print(player.name, end=' ')
        print()

def print_players_count_country_wise(players):
    countries = p.Player.get_countries()
    for country in countries:
        count = 0
        for player in players:
            if player.country == country:
                count += 1
        print (f'{country} has {count} players')

def print_total_runs_country_wise(players):
    countries = p.Player.get_countries()
    for country in countries:
        total_runs = 0
        for player in players:
            if player.country == country:
                total_runs += player.runs
        print (f'{country} has {total_runs} total runs')

def main():
    players = []
    read_data(players)
    print_player_names_country_wise(players)
    print_players_count_country_wise(players)
    print_total_runs_country_wise(players)

main()

