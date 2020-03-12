import csv


def write_csv(users, filename):
    global users_csv, arr_r
    with open("users.csv", "w", newline="") as users_csv:  # newline="" исп для удаление пробела
        csv_w = csv.writer(users_csv)
        csv_w.writerows(users)


def read_csv(filename):
    global users_csv
    with open("users.csv", "r", newline="") as users_csv:
        csv_r = csv.reader(users_csv)
        for row in csv_r:
            arr_r.append(row)


if __name__ == '__main__':
    users = [
        ["Tom", 1234],
        ["Bob", 23456]
    ]
    filename = "users.csv"
    write_csv(users, filename)

    #filename = "users.csv"
    filename = input ("Enter filename")
    arr = read_csv(filename)
    print(arr_r)