def sum():
    status = False
    sum = 0

    while status == False:
        numbers = input("Введите числа через пробел или q для выхода: ").split()
        sum_0 = 0
        for i in range(len(numbers)):
            if numbers[i] == 'q' or numbers[i] == 'Q':
                status = True
                break
            else:
                sum_0 = sum_0 + int(numbers[i])
        sum = sum_0 + sum
    print(f"Сумма: {sum}")

sum()

