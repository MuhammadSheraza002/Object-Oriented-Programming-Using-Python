def near_hundred(n):
  if (abs(100-n)<=10 or abs(200-n)<=10):
      return True
  else:
      return False

def main():
    print(near_hundred(93))
    print(near_hundred(90))
    print(near_hundred(89))

main()
