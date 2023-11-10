def x_power_n(x,n,i = 0,product=1):
    if n== 1 :
        return x
    elif i == n:
        return product
    return x_power_n(x,n,i=i+1,product=product*x)

def main():
    print(x_power_n(3,10))

main()