'''
We have triangle made of blocks. The topmost row has 1 block, the next row down
has 2 blocks, the next row has 3 blocks, and so on. Compute recursively
 the total number of blocks in such a triangle with the given number of rows.

triangle(0) → 0
triangle(1) → 1
triangle(2) → 3
'''

def triangle(n):
    if n <=0:
        return 0
    return n + triangle(n-1)

print(triangle(0))
print(triangle(1))
print(triangle(2))
print(triangle(7))

