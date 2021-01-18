num = 1
string = input('Введите слова через пробел (в конеце пробел не ставьте):')
str_list = string.split()
try:
    for i in range(string.count('')):
        length = len(str_list[i])-1
        if length <= 10:
            print(f"{num} {str_list[i]}")
        else:
            print(f"{num} {str_list[i] [0:9]}")
        num +=1
except: IndexError