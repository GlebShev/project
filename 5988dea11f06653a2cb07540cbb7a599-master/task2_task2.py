c = int(input("Укажите длину списка:"))
my_list = []

for i in range(c):
    element = input("Название:")
    my_list.append(element)

for items in range(int(len(my_list)/2)):
     my_list[items], my_list[items+1] = my_list[items +1], my_list[items]
     items +=1
print(my_list)