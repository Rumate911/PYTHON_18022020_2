def count_positive_value(a,b,c):
    x = 0
    if a > 0:
        x += 1
    if b > 0:
        x += 1
    if c > 0:
        x += 1
    print("Result positive", x)
def count_negative_value(a,b,c):
    x = 0
    if a < 0:
        x += 1
    if b < 0:
        x += 1
    if c < 0:
        x += 1
    print("Result negative", x)

count_negative_value(1,2,4)
count_positive_value(-1,-4,8)