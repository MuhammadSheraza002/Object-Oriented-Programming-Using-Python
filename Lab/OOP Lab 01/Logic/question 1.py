'''
We want to make a row of bricks that is goal inches long.
 We have a number of small bricks (1 inch each) and big
 bricks (5 inches each). Return true if it is possible
 to make the goal by choosing from the given bricks.
 This is a little harder than it looks and can be done
 without any loops. See also: Introduction to MakeBricks
'''


def make_bricks(small, big, goal):
    if goal <= small + big*5:
        return True
    return False


print(make_bricks(3, 1, 8))
print(make_bricks(3, 1, 9))
print(make_bricks(3, 2, 10))