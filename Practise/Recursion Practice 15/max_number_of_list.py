import random as r

def max_number(list,max,i=0):
    if i == len(list):
        return max
    if max < list[i]:
        max = list[i]
    return max_number(list,max,i=i+1)

def main():
    list = [r.randint(10,50) for i in range(5)]
    print(list)
    print(max_number(list,list[0]))

main()
