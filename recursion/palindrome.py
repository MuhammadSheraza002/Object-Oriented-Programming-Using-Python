def main(s,n,i=0,j=0):
    if j == -1 and i == n:
        return True
    if s[i] != s[j]: return False
    return main(s,n,i+1,j-1)
print(main('ababa',5,0,4) )
