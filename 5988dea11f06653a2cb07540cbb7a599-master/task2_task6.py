count = int(input('Введите количество позиций:'))
my_list_all = []
my_list= []
my_dict = {}
name_dict = []
price_dict = []
quanti_dict = []
for i in range(count):
    name = input('Введите название предмета:')
    price = input('Введите цену предмета:')
    quantity = input("Введите количество предметов")

    name_dict.append(name)
    price_dict.append(price)
    quanti_dict.append(quantity)

    my_dict = {"Название:": name, "Цена:": price, "Количестово:": quantity }
    my_list = [f"{i+1}, {my_dict}"]
    my_list_all.append(my_list)

print(my_list_all)
print("Названия:", name_dict,
      "Цена:", price_dict,
      "Количестов:", quanti_dict
    )


