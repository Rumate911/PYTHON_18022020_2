a = int(input("Number 'А': "))
b = int(input("Number 'B': "))
c = int(input("Number 'C': "))
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