with open('task_2.txt') as  file:
    line = file.readlines()
print(f"Количестов строк: {len(line)}")
for i, line in enumerate(line):
    print(f"Строка{i+1} содержит – {len(line.split())} слова")
