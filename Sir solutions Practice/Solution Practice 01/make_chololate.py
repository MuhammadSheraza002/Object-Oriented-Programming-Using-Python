def make_chocolate(small, big, goal):
  total = big * 5 + small
  if (total==goal):
    return small
  elif (total<goal):
      return -1
  elif(total-goal<small):
    return goal - big * 5
  n_big = goal // 5
  if ( ( goal - n_big * 5 ) <= small):
    return goal - n_big * 5
  return -1

def main():
    print(make_chocolate(4, 1, 9))
    print(make_chocolate(4, 1, 10))
    print(make_chocolate(4, 1, 7))

main()
