import random as r

def find_max_index(list, i=0):
    if i + 1 == len(list):  return i
    max_index = find_max_index(list, i+1)
    if list[max_index] > list[i]:   return max_index
    else:   return i

def main():
    x = [r.randint(1,9) for i in range(5)]
    print (x)
    print(find_max_index(x))

main()

