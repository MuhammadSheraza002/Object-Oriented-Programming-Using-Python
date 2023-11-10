list = [[98 ,62 ,66 ,40, 90],
        [59,79,31,38,92],
        [70,72 ,48,50, 29],
        [97 ,17,72,53,41],
        [66 ,22 ,36, 36 ,50]]

for row in range(5):
    max = list[row][0]
    max_index = 0
    for col in range(5):
        if max < list[row][col]:
            max = list[row][col]
            max_index = col
    print('Row %d: %d is at index %d'%(row+1,max,max_index))

