def get_max_power_of_2(n):
    i = 0
    while (2**i<=n):
        i += 1
    return i-1

def express_in_power_of_2(n):
    while (n>1):
        p = get_max_power_of_2(n)
        print(f'{2}^{p}',end='')
        n = n - 2 ** p
        if n>0:
              print('+',end='')
    if n == 1:
        print('2^0')
        
def main():
    n = int(input())
    express_in_power_of_2(n)
              
main()
              
              
