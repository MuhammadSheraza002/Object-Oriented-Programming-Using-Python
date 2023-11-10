def compare_strings(w1, w2):
    length = min(len(w1), len(w2))
    for i in range(length):
        if w1[i] > w2[i]:
            return 1
        elif w1[i] < w2[i]:
            return -1
    if length < len(w1):
        return 1
    elif length < len(w2):
        return -1
    return 0

def strings1():
    w1 = input("Enter any string:")
    w2 = input("Enter any string:")
    res = compare_strings(w1, w2)
    if res == 0:
        print ("Both are equal")
    elif res > 0:
        print ("String 1 is greater")
    else:
        print ("String 2 is greater")

strings1()


