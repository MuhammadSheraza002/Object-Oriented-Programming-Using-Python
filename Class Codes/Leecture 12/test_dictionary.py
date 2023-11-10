import random as r

class Player:
    players_count = 0
    def __init__(self):
        Player.players_count += 1
        self.__pn = Player.players_count
        self.__match_count = r.randint(1,50)
        self.__runs = r.randint(50,1500)
        self.__wkts = r.randint(0,100)
    def __str__(self):
        return f'{self.__pn}\t{self.__match_count}\t{self.__runs}\t{self.__wkts}'
    def get_pn(self):
            return self.__pn
def main():
    dictionary={}
    for i in range(10):
        player = Player()
        dictionary[player.get_pn()]=player

    for i in range(1,11):
        print (dictionary.get(i))
    #an alternate loop
    #for tuple in dictionary:
        #print(dictionary.get(tuple))
    #another alternate loop
    #for player in dictionary.values():
        #print(player)


main()
