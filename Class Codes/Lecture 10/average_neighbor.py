import random as r

def average_neighbor(arr):
    for i in range(1, len(arr)-1):
        arr[i] = int((arr[i-1]+arr[i+1])/2)

def main():
    arr = [r.randint(0,10) for i in range(10)]
    print(arr)
    average_neighbor(arr)
    print(arr)

main()
