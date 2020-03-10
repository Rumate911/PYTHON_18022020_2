def main_sort_ex():
    arr = [12, 32, 5, 456, 84, 25, 546, 78, 98, 45, 21, 1]
    print(arr)
    arr.sort()
    print(arr)


def matrix_example():
    users = [
        [11, 12, 13],
        [21, 22, 23]
    ]
    for i in range(2):
        for j in range(3):
            print(users[i][j])

def matrix_ex_ch():
    users = [
        ["Tom", 32, "+380675668494"],
        ["Bob", 32, "+380675668495"],
        ["Alice", 19, "+380675668475"]
    ]
    for user in users:
        if (user[1] > 20):
            print(user)

def main_txt():
    arr = [1,2,3,56,21,35]
    with open("int_arr.txt", "w") as int_file:
        for i in arr:
            int_file.write(str(i)+";")

def main_csv():
    arr = [1,2,3,56,21,35]
    arr1 = [1, 1, 1, 1, 1, 1]
    with open("int_arr.csv", "w") as file:
        count = 0
        for i in arr1:
            file.write(str(i)+";")
        file.write("\n\r")
    arr_head =[]
    with open("int_arr.txt","r") as read_file:
        for row in read_file:
            print(row)
            list_str=row.split(";")
            for word in list_str:
                arr_read.append(int(word))
            print(arr_read)
if __name__ == '__main__':
    main_csv()

