def count8(n,sum=0):
    if n // 10 == 0:
        if n == 8:
            sum+=1
        return sum
    if n % 10 == 8:
        n = n // 10
        if n % 10 == 8:
            sum += 1
        sum += 1
        return count8(n,sum)
    return count8(n//10,sum)

print(count8(8))
print(count8(818))
print(count8(8818))