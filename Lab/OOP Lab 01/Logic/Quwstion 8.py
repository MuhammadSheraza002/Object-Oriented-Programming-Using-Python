'''
Return True if the given string contains an appearance of "xyz" where the xyz
is not directly preceeded by a period (.). So "xxyz" counts but "x.xyz" does
not.
xyz_there('abcxyz') → True
xyz_there('abc.xyz') → False
xyz_there('xyz.abc') → True
'''

def xyz_there(str):
    for index in range(len(str)):
      if str[index] == 'x':
          if str[index:index+3] =='xyz':
              if index > 0 and str[index-1] == '.':
                  continue
              return True

    return False

print(xyz_there('abcxyz'))
print(xyz_there('abc.xyz'))
print(xyz_there('xyz.abc') )

