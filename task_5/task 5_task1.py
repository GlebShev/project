with open('text.txt', 'w') as file_1:
    while True:
        line = input('Введите строку:')
        if line == '':
            break
        file_1.writelines(line + '\n')
