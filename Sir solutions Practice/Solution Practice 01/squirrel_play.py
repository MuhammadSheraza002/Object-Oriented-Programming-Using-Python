def squirrel_play(temp, is_summer):
  if (is_summer==True and temp>=60 and temp<=100):
    return True
  elif (is_summer==False and temp>=60 and temp<=90):
    return True
  return False

def main():
    print(squirrel_play(70, False))
    print(squirrel_play(95, False))
    print(squirrel_play(95, True))

main()
