'''
Return True if the string "cat" and "dog" appear the same number of times in
the given string.
cat_dog('catdog') → True
cat_dog('catcat') → False
cat_dog('1cat1cadodog') → True
'''


def count_dog_and_cat(string,dog_cat):
    count = 0
    for index in range((len(string)-len(dog_cat))+1):
        if string[index:index+len(dog_cat)] == dog_cat:
            count += 1
    return count

def cat_dog(string):
    return count_dog_and_cat(string,'cat') == count_dog_and_cat(string,'dog')

print(cat_dog('catdog'))
print(cat_dog('catcat'))
print(cat_dog('1cat1cadodog'))