def countHi(s,sum=0,i=0):
    if i == len(s)-2:
        if s[i:i+1]=='hi':
            sum +=1
        return sum

    if s[i:i+2] == 'hi':
        sum+=1

    return countHi(s,sum,i+1)

print(countHi("xxhixx"))
print(countHi("xhixhihihihix"))
print(countHi("hi"))
