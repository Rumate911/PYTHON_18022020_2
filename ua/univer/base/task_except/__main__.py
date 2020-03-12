
def error(): pass
'''    try:
        x = int(input("Enter int "))
        x/0
        print (x)
    except Exception as e:
        print("Not int", e) '''


def validate_int_input():
    while True:
        try:
            print("Enter int in position", i)
            x = int(input())
            print (x)
            break
        except Exception as e:
            print("Not int", e)
    arr.append(x)

def valid_mark():
    while True:
        try:
            mark = validate_int_input()
            if mark > 12 or mark < 0:
                raise Exception("not valid mark, 0 < mark <12 ")
            break
        except Exception as e:
            print(e)
            with open("my.log", "a") as log:
                log.write(f"{datetime.now()} {e} \r")
    return mark
if __name__ == "__main__":
    arr = []
    for i in range(5):
        x = valid_mark()
        arr.append(x)