list_1 = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
answer = [el for num, el in enumerate(list_1) if list_1[num - 1] < list_1[num]]
print(answer)