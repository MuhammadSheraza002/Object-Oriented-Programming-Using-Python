def print1to50_5_in_each_row():
    for i in range(1, 51):
        print (f'{i:2d}', end=" ")
        if i % 5 == 0:
            print()

print1to50_5_in_each_row()
