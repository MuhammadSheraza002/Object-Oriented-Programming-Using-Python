
def start_loop(n):
    i = 0
    count = i
    while 2**i <= n:
        count=i
        i+=1
    return count

def main():
    n = int(input())
    i = start_loop(n)
    sum = 0
    while sum < n and i >=0:
        print(f'{2}^{i}',end='+')
        sum+=2**i
        i-=1
    print('\b')

main()