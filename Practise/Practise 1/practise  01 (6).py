'''"""Given two strings, return True if either of the strings appears at the very end
of the other string, ignoring upper/lower case differences (in other words, the
computation should not be "case sensitive"). Note: s.lower() returns the lowercase
version of a string."""

def end_other(str1, str2):
    if len(str1) < len(str2):
        for index in range(len(str2)-len(str1)):
            if str2[index:index+len(str1)] == str1:
                return True
        return False
    if len(str2) < len(str1):
        for index in range(len(str1)-len(str2)):
            if str1[index:index+len(str2)] == str2:
                return True
        return  False



print(end_other('Hiabc', 'abc'))
print(end_other('AbC', 'HiaBc'))
print(end_other('abc', 'abXabc'))'''

def end_other(str1, str2):
    if len(str1) > len(str2):
        return str1[0:len(str2)] == str2 or str1[len(str1)-len(str2):len(str1)] == str2

    if len(str2) > len(str1):
        return str2[0:len(str1)] == str1 or str2[len(str2) - len(str1):len(str2)] == str1




print(end_other('Hiabc', 'abc'))
print(end_other('AbC', 'HiaBc'))
print(end_other('abc', 'abXabc'))