'''
Given a non-negative int n, return the sum of its digits recursively (no loops).
Note that mod (%) by 10 yields the rightmost digit (126 % 10 is 6), while divide
(/) by 10 removes the rightmost digit (126 / 10 is 12).
sumDigits(126) → 9
sumDigits(49) → 13
sumDigits(12) → 3
'''
def sumDigits(n):
    if n // 10 == 0:
        return n
    return n%10 + sumDigits(n//10)

print(sumDigits(2))
print(sumDigits(126))
print(sumDigits(49) )
print(sumDigits(12))