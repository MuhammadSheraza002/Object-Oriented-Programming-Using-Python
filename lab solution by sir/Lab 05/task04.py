#convert upper case to lower case letters
def toupper():
    word = "AbcDefG"
    print (word)
    new_word = ""
    for character in word:
        if character >= 'A' and character <= 'Z':
            new_word += chr(ord(character) | 32)
        else:
            new_word += character
    print (new_word)

toupper()
