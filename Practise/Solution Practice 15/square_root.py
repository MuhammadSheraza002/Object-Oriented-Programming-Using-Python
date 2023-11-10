EPSILON = 0.000001     #In mathematics, epsilon is some small number that can be considered zero
def square_root (x, sq = 1):
    if abs(x/sq - sq) < EPSILON:
        return sq
    return square_root(x, (sq + x/sq) / 2)

def main():
    print(square_root(5))
    print(square_root(0.25))
    print(square_root(2.25))

main()

