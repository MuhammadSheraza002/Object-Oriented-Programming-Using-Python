list = [[98 ,62 ,66 ,40, 90],
        [59,79,31,38,92],
        [70,72 ,48,50, 29],
        [97 ,17,72,53,41],
        [66 ,22 ,36, 36 ,50]]


for row in range(5):
    for col in range(5):
        print(list[row][col],end=' ')
    print()

sum_col_of_list = [0] * 5
for col in range(5):
    sum = 0
    for row in range(5):
        sum+=list[row][col]
    sum_col_of_list[col] = sum

for i in range(len(sum_col_of_list)):
    print(sum_col_of_list[i],end=' ')