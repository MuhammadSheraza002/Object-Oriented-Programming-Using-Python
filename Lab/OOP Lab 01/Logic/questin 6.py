'''
Given three ints, a b c, return True if one of b or c is "close" (differing from
 a by at most 1), while the other is "far", differing from both other values by
  2 or more. Note: abs(num) computes the absolute value of a number

'''
def close_far(a,b,c):
    if abs(b-a)>=2 and abs(c-a) >=2 and abs(b-c)>=2:
        return False
    return  abs(b-a)<=1 or abs(c-a) <=1

print(close_far(1, 2, 10))
print(close_far(1, 2, 3))
print(close_far(4, 1, 3))

