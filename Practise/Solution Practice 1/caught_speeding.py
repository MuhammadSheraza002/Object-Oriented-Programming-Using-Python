def caught_speeding(speed, is_birthday):
  if (is_birthday==True and speed<=65):
    return 0
  if (speed<=60):
    return 0
  elif (is_birthday==True and speed<=85):
    return 1
  elif (speed<=80):
    return 1
  else:
    return 2

def main():
    print(caught_speeding(60, False))
    print(caught_speeding(65, True))
    print(caught_speeding(65, False))

main()
