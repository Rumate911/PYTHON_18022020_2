def count_positive_value():
    a = int(input("Number 'А': "))
    b = int(input("Number 'B': "))
    c = int(input("Number 'C': "))
    x = 0
    if a > 0:
        x += 1
    if b > 0:
        x += 1
    if c > 0:
        x += 1
    print("Result positive", x)
def count_negative_value(): '''Для значений в def count_negative_value(а,b,c) можно сокращать условия отбора если нас интересуют в условиях отбора'''
    a = int(input("Number 'А': "))
    b = int(input("Number 'B': "))
    c = int(input("Number 'C': "))
    x = 0
    if a < 0:
        x += 1
    if b < 0:
        x += 1
    if c < 0:
        x += 1
    print("Result negative", x)
count_negative_value() '''Для значений в count_negative_value(1,-7,4) для отбора '''
count_positive_value()

x = int(input("Number 'X': "))
y= int(input("Number 'Y': "))
z = int(input("Number 'Z': "))
count_negative_value(x,y,z) '''Для использования повторного кода через def '''
count_positive_value(x,y,z)
