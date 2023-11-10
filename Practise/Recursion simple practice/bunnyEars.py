def bunnyEars(n):
    if n <=0:
        return 0

    if n == 1:
        return 2
    return 5 + bunnyEars(n-2)

print(bunnyEars(0))
print(bunnyEars(1))
print(bunnyEars(2))
print(bunnyEars(7))
