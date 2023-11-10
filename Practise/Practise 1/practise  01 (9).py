def count_dog_and_cat(string,dog_cat):
    count = 0
    for index in range(len(string)-len(dog_cat)):
        if string[index:index+len(dog_cat)] == dog_cat:
            count += 1
    return count
def cat_dog(string):
    return count_dog_and_cat(string,'cat') == count_dog_and_cat(string,'dog')

print(cat_dog('catdog'))
print(cat_dog('catcat'))
print(cat_dog('1cat1cadodog'))