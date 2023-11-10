from pickle import *
from tournament import *

file = open('fifa.csv', 'r')
tournament = Tournament(file)
file.close()
string = dumps(tournament)
print (string)
input('\nRead serialization string and press enter to see next output')
print() #leave a blank line
tournament1 = loads(string)
print (tournament1)
