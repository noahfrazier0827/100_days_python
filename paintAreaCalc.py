import math

def paint_calc():
    x = ((test_h * test_w)/coverage)
    print(math.ceil(x))

test_h = int(input("Height of wall: "))
test_w = int(input("Width of wall: "))
coverage = 5

paint_calc()
