def get_binary_string(x, b=''):
    if x == 0:  return b
    if x == 1:  return '1'+ b
    r = x % 2
    if r==0 and b=='':   b='0'
    elif r==0:   b = '0' + b
    else:   b = '1' + b
    return get_binary_string(int(x/2), b)

def main():
    print(get_binary_string(6))
    print(get_binary_string(15))
    print(get_binary_string(9))
    print(get_binary_string(63))
    print(get_binary_string(12))
    print(get_binary_string(14))
    print(get_binary_string(29))
    print(get_binary_string(26))

main()
