import random as r

def is_sum_possible(x, sum, i=0,j=0):
    print(j)
    if sum == 0:    return True,j
    if i == len(x): return False,j
    is_possible = False,j
    if x[i] <= sum:
        is_possible = is_sum_possible(x, sum-x[i], i+1,j+1)
    if is_possible == True: return True,j
    return is_sum_possible(x, sum, i+1,j+1)

def main():
    x = [25, 45, 67, 84, 90]
    print (is_sum_possible(x, 115))
    print (is_sum_possible(x, 174))
    print (is_sum_possible(x, 241))
    print (is_sum_possible(x, 286))
    print (is_sum_possible(x, 311))
    print (is_sum_possible(x, 92))
    print (is_sum_possible(x, 116))
    print (is_sum_possible(x, 173))
    print (is_sum_possible(x, 240))
    print (is_sum_possible(x, 288))
    print (is_sum_possible(x, 313))
    print (is_sum_possible(x, 94))

main()


