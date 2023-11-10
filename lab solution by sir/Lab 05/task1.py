def read_file():
    file = open("sentences.txt","r")
    lines=[]
    for line in file:
        lines.append(line)
    return lines

def toupper(lines):
    newlines=[]
    for line in lines:
        newline=""
        for character in line:
            if character >='A' and character <= 'Z':
                newline+=chr(ord(character) | 32)
            else:
                newline+=character
        newlines.append(newline)
    return newlines

def write_file(lines):
    file = open("small_sentences.txt","w")
    for line in lines:
        file.write(f'{line}')

def task1():
    lines = read_file()
    newlines = toupper(lines)
    write_file(newlines)

task1()
