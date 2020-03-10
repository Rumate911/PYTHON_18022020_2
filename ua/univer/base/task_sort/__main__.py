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

def main():
    users = [
        ["Tom", 32, "+380675668494"],
        ["Bob", 32, "+380675668495"],
        ["Alice", 19, "+380675668475"]
    ]
    for user in users:
        if(user[1]>20):
            print(user)

if __name__ == '__main__':
    main()

