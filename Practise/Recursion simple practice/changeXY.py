'''
Given a string, compute recursively (no loops) a new string where all the lowercase
'x' chars have been changed to 'y' chars.
changeXY("codex") → "codey"
changeXY("xxhixx") → "yyhiyy"
changeXY("xhixhix") → "yhiyhiy"
'''

def changeXY(s,i=0,ns=''):
    if len(s)==i:
        return ns
    if s[i] == 'x':
        ns+='y'
    else:
        ns += s[i]
    return changeXY(s,i+1,ns)

print(changeXY("codex"))
print(changeXY("xxhixx"))
print(changeXY("xhixhix"))