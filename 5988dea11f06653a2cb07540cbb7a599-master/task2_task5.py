my_list = [7, 6, 5, 5, 3]
num = int(input("Введите число:"))
my_list.append(num)
my_list.sort(reverse=True)

print(f"Рейтинг: {my_list}")