from ua.univer.base.tasks_while.task_3 import Task_2_CW, num_99_t_1

# return выйти с функции
def task_3_CW(a,b):
    n = 0
    if a < b:
        for i in range(a, b + 1):
            print(i)
            n += 1
    else:
        print(" not a < b ")
    print("count = ", n)


def menu():
    while True:
        begin = int(input("Enter begin"))
        end = int(input("Enter end"))
        task_3_CW(begin, end)
        answer = input("Exit[y/n]")
        if answer == "y":
            break


if __name__== "__main__":
    for i in range(10):
        for j in range (10):
            if (i==0 or i==9) and (j==0 or j==9):
                print("* ", end="")
            else:
                print("* ", end="")
        print()

