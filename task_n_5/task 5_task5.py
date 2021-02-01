with open('task_5.txt', 'w') as file:
    numbers =  input('Введите числа через пробел: ')
    file.write(numbers)

num_list = map(int, numbers.split())
print(sum(num_list))
