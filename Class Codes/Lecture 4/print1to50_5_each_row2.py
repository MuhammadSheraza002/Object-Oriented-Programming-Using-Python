def print1to50_5_in_each_row():
    k = 1
    for i in range(10):
        for j in range(5):
            print (f'{k:2d}', end=" ")
            k += 1
        print()
        
print1to50_5_in_each_row()
