
def paint_calc(height, width, cover):
    area = height * width
    ans = round(area / cover)
    print(f"You will need {ans} cans of paint.")


test_h = int(input("Height of wall: "))
test_w = int(input("Width of wall: "))
coverage = 5
paint_calc(height=test_h, width=test_w, cover=coverage)