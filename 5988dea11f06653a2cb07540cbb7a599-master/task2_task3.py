sesons_list = ["Winter", "Spring", "Summer", "Autumn"]
sesons_dict = {1: "Winter", 2: "Spring", 3: "Summer", 4: "Autumn"}
month = int(input("Введите номер месяца:"))
if month == 12 or month == 1 or month == 2:
    print(sesons_list[0])
    print((sesons_dict.get(1)))
elif month == 3 or month == 4 or month == 5:
    print(sesons_list[1])
    print((sesons_dict.get(2)))
elif month == 6 or month == 7 or month == 8:
    print(sesons_list[2])
    print((sesons_dict.get(3)))
elif month == 9 or month == 10 or month == 11:
    print(sesons_list[3])
    print((sesons_dict.get(4)))
else:
    print("Вы не правильно ввели номер месяца")
