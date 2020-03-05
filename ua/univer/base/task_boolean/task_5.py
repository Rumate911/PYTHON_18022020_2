def logic_algoritm_1():
    a = input("Укажите значение 'А': ")
    print(a.isdigit()) # isdigit проверка на символы или число, также если есть - то возратит False
def logic_algoritm_2_3():
    a = int(input("Enter a number: "))
    if a % 2 == 0: # четное то которое делится на 2 (%2) остатком от деления
        print('Even number')
    else:
        print('Odd number') # обратный результат зачисляем к нечетным
def logic_algoritm_4():
    a = int(input("Enter 'A' number: "))
    b = int(input("Enter 'B' number: "))
    print("Result 'A'", a > 2)
    print("Result 'B'", b <= 3)
def logic_ajgoritm_5():
    a = int(input("Enter 'A' number: "))
    b = int(input("Enter 'B' number: "))
    print("Result 'A'", a > 0)
    print("Result 'B'", b <= -2)