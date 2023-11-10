import random

t = random.randint(5, 9)
print ("Table No: ", t)
def print_table():
    for i in range(1, 11):
        print (t,"\t*\t",i,"\t=\t", t*i)

print_table()
