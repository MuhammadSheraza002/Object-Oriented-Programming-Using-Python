def substring(s1,s2,i1=0,i2=0):
    if i1 == len(s1) and i2 < len(s2):
        return False
    if i2 == len(s2):
        return True
    if s1[i1] == s2[i2]:
        return substring(s1,s2,i1+1,i2+1)
    return substring(s1, s2, i1 + 1, i2)

s1 = input()
s2 = input()
print(substring(s1,s2))