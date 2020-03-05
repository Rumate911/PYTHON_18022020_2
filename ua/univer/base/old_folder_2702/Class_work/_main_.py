from ua.univer.base.Class_work.task_work_1 import count_positive_value, count_negative_value


def enter_int():
    return int(input("Number: "))


if __name__=="__main__":
    print("Hi main")
    count_negative_value(1,2,4)
    count_positive_value(-1,-4,8)

    x = enter_int()
    y = enter_int()
    z = enter_int()
    count_negative_value(x, y, z)
    count_positive_value(x, y, z)