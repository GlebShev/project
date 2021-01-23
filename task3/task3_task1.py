def division(num1, num2):
    try:
        answer = num1/num2
        return answer
    except ZeroDivisionError:
        print("Деленить на ноль нельзя")


print(division(10, 2))
print(division(10, 0))

