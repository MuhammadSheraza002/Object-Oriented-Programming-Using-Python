from pickle import *
from tournament import *

file = open('tournament.bin','rb')
tournament = load(file)
print(tournament)
file.close()
