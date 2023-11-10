def table(number):
    print("Table no: ",number)
    for i in range(1,11):
        print(f"{number}\t*\t{i}\t=\t{number*i}")
import random
table(random.randint(5,9))
