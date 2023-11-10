def friend_fashion(you, friend):
  if ((you>=8 or friend>=8) and you>2 and friend>2):
    return 2
  elif (you<=2 or friend<=2):
    return 0
  return 1

def main():
    print(friend_fashion(5, 10))
    print(friend_fashion(5, 2))
    print(friend_fashion(5, 5))

main()

