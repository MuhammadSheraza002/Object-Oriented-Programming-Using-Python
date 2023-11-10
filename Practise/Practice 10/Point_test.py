import Point

def main():
    p1 = Point.Point(2,3)
    p2 = Point.Point(-4,6)
    p1.show()
    p1.check_quadrant()
    p1.reverse_point()
    p1.show()
    p1_rotate = p1.rotate_point(90)
    p2_rotate = p2.rotate_point(360)
    print(p1_rotate)
    print(p2_rotate)
    print(p1.compare_rotation(p2))


main()