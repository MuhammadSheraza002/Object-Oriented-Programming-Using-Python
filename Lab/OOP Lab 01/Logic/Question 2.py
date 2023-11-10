'''Given 3 int values, a b c, return their sum. However,
 if one of the values is the same as another of the values,
  it does not count towards the sum.
'''

def lone_sum(a, b, c):
    if a==b and b==c:
        return 0
    elif a==b:
        return c
    elif a==c:
        return b
    elif b== c:
        return a

    return a + b+ c

print(lone_sum(1, 2, 3))
print(lone_sum(3, 2, 3))
print(lone_sum(3, 3, 3))