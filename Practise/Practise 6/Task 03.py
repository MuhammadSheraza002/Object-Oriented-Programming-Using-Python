list = [[98 ,62 ,66 ,40, 90],
        [59,79,31,38,92],
        [70,72 ,48,50, 29],
        [97 ,17,72,53,41],
        [66 ,22 ,36, 36 ,50]]

for index in range(5):
    for j in range(5):
        if index == j:
            print(list[index][index],end=' ')
        else:
            print(' ',end=' ')
    print('')
