'''For practice of coming lab, place file 'cities.csv' in your python program's folder and do read with given code:
The file contains population of each city in 1972, 1981, 1998 & 2017.

Next, do practice to find city with minimum population, maximum population in
particular year. The difference of population for each city in next years. The
maximum difference, the minimum difference. The percentage difference etc.'''
def main():
    file = open("cities.csv","r")
    for f in file:
        s = f.split(',')
        print(s[0])
        print (f'{s[0]}\t{s[1]}\t{int(s[2])}\t{int(s[3])}\t{int(s[4])}\t{int(s[5])}')
    file.close()

main()