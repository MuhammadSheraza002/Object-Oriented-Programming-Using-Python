def hm_sum(n,i = 1,sum=0):
    if i == n:
        return sum + (1/i)
    return sum + hm_sum(n,i = i+1,sum=sum+(1/i))

print(hm_sum(3))

