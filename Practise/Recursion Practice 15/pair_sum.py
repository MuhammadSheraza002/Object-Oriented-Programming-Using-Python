import random as r

def pair_sum(list,max=0,i=0,j=1):
    if i == len(list)-2 and j == len(list)-1:
        return max
    elif j == len(list)-1:
        if list[i]+list[j]>max:
            max=list[i]+list[j]
        return pair_sum(list,max,i+1,i+2)

    else:
        if list[i]+list[j]>max:
            max=list[i]+list[j]

    return pair_sum(list,max,i,j+1)



def main():
    list = [r.randint(1,5) for i in range(5)]
    print(list)
    print(pair_sum(list,list[0]+list[1]))

main()
