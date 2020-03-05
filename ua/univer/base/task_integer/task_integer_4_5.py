def integer_lenght_1(x):
    x = int(input("Введите значение в см: "))
    L = x//100
    print("Результат в м", L)
def integer_kilo(x):
    m = x//1000
    print("Результат в тоннах", m)
def integer_byte_3(x):
    x = int(input("Введите значение в байт: "))
    kilo_byte = x//1024
    print("Результат", kilo_byte)
def integer_5(a,b):
    a = int(input("Укажите длинну отрезка 'А': "))
    b = int(input("Укажите длинну отрезка 'B': "))
    result = a//b
    result1 = a%b
    print("Максимальное кол-во отрезков", result)
    print("Длинна незанятого отрезка", result1)