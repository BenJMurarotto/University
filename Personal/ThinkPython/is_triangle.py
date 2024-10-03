def is_triangle(a, b, c):
    sides = [a,b,c]
    sides.sort()
    if sides[len(sides) - 1] <= sides[0] + sides[1]:
        print("Yes")
    else:
        print("No")





def get_sides():
    print("Please input the size of the triangle side 1: ")
    side1 = int(input())
    print("Please input the size of the triangle side 2: ")
    side2 = int(input())
    print("Please input the size of the triangle side 3: ")
    side3 = int(input())

    return side1, side2, side3

is_triangle(*get_sides())