import player as p

def read_data(players):
    file = open("players.txt", 'r')
    record = file.read()
    lines = record.split('\n')
    file.close()
    for i in range(0, len(lines), 13):
        #name = lines[i], country=lines[i+1], start=lines[i+2], end=lines[i+3], matches=lines[i+4], innings=lines[i+5], notout=lines[i+6], runs=lines[i+7], highest=lines[i+8], average=lines[i+9], hundereds=lines[i+10], fifties=lines[i+11], zeros=lines[i+12]
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

def player_having_longest_span(players):
    longest = 0
    for i in range(1, len(players)):
        if players[longest].end-players[longest].start < players[i].end-players[i].start:
            longest = i
    print(players[longest])

def player_having_most_runs(players):
    highest = 0
    for i in range(1, len(players)):
        if players[highest].runs < players[i].runs:
            highest = i
    print(players[highest])

def player_having_most_hundreds(players):
    highest = 0
    for i in range(1, len(players)):
        if players[highest].hundereds < players[i].hundereds:
            highest = i
    print(players[highest])

def player_having_most_fifties(players):
    highest = 0
    for i in range(1, len(players)):
        if players[highest].fifties < players[i].fifties:
            highest = i
    print(players[highest])

def player_having_highest_score(players):
    highest = 0
    for i in range(1, len(players)):
        if players[highest].highest < players[i].highest:
            highest = i
    print(players[highest])

def players_country(players, country):
    for player in players:
        if player.country == country:
            print(player)
    print ("---------------------------------------------------------------------------------")

def player_having_highest_zeros(players):
    highest = 0
    for i in range(1, len(players)):
        if players[highest].zeros < players[i].zeros:
            highest = i
    print(players[highest])

def main():
    players = []
    read_data(players)
    player_having_longest_span(players)
    player_having_most_runs(players)
    player_having_most_hundreds(players)
    player_having_most_fifties(players)
    player_having_highest_score(players)
    player_having_highest_zeros(players)
    players_country(players, 'Pakistan')
    #for player in players:
     #   print(player)

main()

