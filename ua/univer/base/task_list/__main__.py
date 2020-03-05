def main ():
    arr = [10, 20, 30, 40, 50]
    print(len(arr))
    print(arr[-1])
    print(arr )
def list ():
    companies = ["Microsoft", "Google", "Oracle", "Apple"]
    i = 0
    while i < len(companies):
        print(companies[i])
        i += 1
def main_2 ():
    arr = [10, 20, 30, 40, 50]
    arr[2]=13
    arr.append(1300)
    print(len(arr))
    for x in arr:
        print(x, end=", ")

def main_3 ():
    arr = [10, 20, 30, 40, 50]
    for i in range(5):
        arr.append(i)
    arr.insert(2,100)
    print(len(arr))
    for x in arr:
        print(x, end=", ")

def main_4 ():
    arr = [10, 20, 30, 40, 50]
    for i in range(5):
        arr.append(i)
    arr.remove(0)
    print(len(arr))
    for x in arr:
        print(x, end=", ")

def main_5 ():
    arr = [10, 20, 30, 40, 50]
    for i in range(5):
        arr.append(i)
    arr.insert(2,100)
    arr.remove(0)
    sort_arr = sorted(arr)
    print(len(arr))
    for x in arr:
        print(x, end=", ")
    for x in sort_arr:
            print(x, end=", ")

def main_7 ():
    import random

    a = []
    for i in range(10):
        a.append(i, end-'')

    print(a)

    even = 0
    odd = 0

    for i in a:
        if i % 2 == 0:
            even += 1
        else:
            odd += 1
    print("Even:", even)
    print("Odd:", odd)

def main_6 ():
    #import random

    a = []
    for i in range(10):
        a.append(int(random.random() * 100))

    print(a)

    even = 0
    odd = 0

    for i in a:
        if i % 2 == 0:
            even += 1
        else:
            odd += 1

    print("Even:", even)
    print("Odd:", odd)

def main_8():
    arr_positive = []
    for x in range (-10,10,1):
        if x % 2 == 1:
            arr_positive.append(x)

    print(arr_positive)

def main_9():
    values = []
    start = 1;
    end = 10;
    for i in range(start, end):
        value = int(input("Enter int value - "+"["+str(i)+"/"+str(end)+")] "))
        values.append(value)
    print(values)

if __name__ == "__main__":
    # main()
    main_9()