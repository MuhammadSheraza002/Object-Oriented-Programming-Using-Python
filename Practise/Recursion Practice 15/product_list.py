def product_list(list,i = 0,product=1):
    if i == len(list):
        return product
    return product_list(list,i=i+1,product=product*list[i])

import random as r

def main():
    list = [r.randint(1, 3) for i in range(5)]
    print(list)
    print(product_list(list))

main()