def calculate_complex_rate(rate,money,period):
    month_sum = money
    for i in range(1,period+1):
        month_sum = round(month_sum + month_sum*(rate/100/12),2)
        print(i,month_sum)
    return month_sum


def calculate_simple_rate(rate,money,period):
    for i in range(1,period+1):
        result_sum = round(money + money*(rate/100/12)*i,2)
        print(i,result_sum)
    return result_sum

def main():
    choice = "y"
    while choice == "y":
        money, period, rate = input_data()
        print(" 1. calculate_simple_rate")
        print(" 2. calculate_simple_rate")
        option = int(input("Enter type of rate "))
        if option == 1 :
            result1 = calculate_simple_rate(rate,money,period)
            print(result1)
        if option == 2:
            result2 = calculate_complex_rate(rate, money, period)
            print(result2)
        choice = input("Again{y/n}")


def input_data():
    rate = int(input("Введите процентную ставку: "))
    money = int(input("Введите сумму: "))
    period = int(input("Введите период ведения счета в месяцах: "))
    return money, period, rate


if __name__== "__main__":
    main()