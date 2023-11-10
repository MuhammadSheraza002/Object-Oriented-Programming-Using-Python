import random as r

def is_sum_possible(x, sum, elements, i=0):
    if sum == 0:    return True
    if i == len(x): return False
    is_possible = False
    count_elements = len(elements)
    if x[i] <= sum:
        elements.append(x[i])
        is_possible = is_sum_possible(x, sum-x[i], elements, i+1)
        if is_possible == False:
            elements.pop(-1)
    if is_possible == True: return True
    return is_sum_possible(x, sum, elements, i+1)

def main():
    x = [25, 45, 67, 84, 90]
    elements=[]
    if is_sum_possible(x, 115, elements):
        print(elements)
    else:
        print('Not Possible')
    elements=[]
    if is_sum_possible(x, 174, elements):
        print(elements)
    else:
        print('Not Possible')
    elements=[]
    if is_sum_possible(x, 241, elements):
        print(elements)
    else:
        print('Not Possible')
    elements=[]
    if is_sum_possible(x, 286, elements):
        print(elements)
    else:
        print('Not Possible')
    elements=[]
    if is_sum_possible(x, 311, elements):
        print(elements)
    else:
        print('Not Possible')
    elements=[]
    if is_sum_possible(x, 92, elements):
        print(elements)
    else:
        print('Not Possible')
    elements=[]
    if is_sum_possible(x, 116, elements):
        print(elements)
    else:
        print('Not Possible')

main()


