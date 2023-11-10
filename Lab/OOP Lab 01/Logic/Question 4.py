'''Given 3 int values, a b c, return their sum. However, if any of the values is a
teen -- in the range 13..19 inclusive -- then that value counts as 0, except 15
and 16 do not count as a teens. Write a separate helper "def fix_teen(n):"that
takes in an int value and returns that value fixed for the teen rule. In this
way, you avoid repeating the teen code 3 times (i.e. "decomposition"). Define
the helper below and at the same indent level as the main no_teen_sum().'''

def is_teen(age):
    if age <=19 and age>=13:
        if age==15 or age ==16:
            return False
        return True
    return False
def no_teen_sum(a, b, c):
    my_tuple = a,b,c
    sum = 0
    for index in range(len(my_tuple)):
        if is_teen(my_tuple[index])==False:
            sum+=my_tuple[index]
    return sum

print(no_teen_sum(1, 2, 3) )
print(no_teen_sum(2, 13, 1))
print(no_teen_sum(2, 1, 14))
