from pickle import *
from tournament import *

file = open('fifa.csv', 'r')
tournament = Tournament(file)
file.close()
file = open('tournament.bin','wb')
dump(tournament, file)
file.close()

