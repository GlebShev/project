with open('task_4.txt') as file1:
    lines = file1.readlines()

with open('task_4_new.txt', 'w') as file2:
    for line in lines:
        if '1' in line:
            line = line.replace('One', 'Один')
        elif '2' in line:
            line = line.replace('Two', 'Два')
        elif '3' in line:
            line = line.replace('Three', 'Три')
        elif '4' in line:
            line = line.replace('Four', 'Четыре')
        file2.write(line)
        