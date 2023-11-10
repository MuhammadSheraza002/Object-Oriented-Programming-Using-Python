import random
def main():
    count = 0
    for i in range(10):
        x = random.randint(0,100)
        print(x)
        if x<50:
            count +=1
    return f"{count} numbers are less than 50"
print(main())
