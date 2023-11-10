import random as r

def find_max(list, i=0):
    if i + 1 == len(list):  return list[i]
    max = find_max(list, i+1)
    if max > list[i]:   return max
    else:   return list[i]

def main():
    x = [r.randint(1,9) for i in range(5)]
    print (x)
    print(find_max(x))

main()

