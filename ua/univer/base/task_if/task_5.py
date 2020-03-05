def construction_more_1(x):
    x = int(input("Введите значени: "))
    if x>20:
        print("hello in club")
    else:
        print("go home")
def construction_2_3(a):
    if a > 0:
        print("Result + number", a + 1)
    elif a < 0:
        print("Result - number", a - 2)
    else:
        print("Result 0 number", a + 10)
def construction_more_4(a,b,c):
    x = 0
    if a > 0:
        x += 1
    if b > 0:
        x += 1
    if c > 0:
        x += 1
    print("Result", x)
def construction_more_less_5(a, b, c):
    x = 0
    y = 0
    if a > 0:
        x += 1
    elif a < 0:
        y += 1
    if b > 0:
        x += 1
    elif b < 0:
        y += 1
    if c > 0:
        x += 1
    elif c < 0:
        y += 1
    print("Result +", x )
    print("Result -", y )