sub  = dict()
with open('task_6.txt') as file:
    lines = file.readlines()

for line in lines:
    new_line = line.split()
    subject = new_line[0]
    lessens = sum([int(i[:i.find('(')]) for i in new_line[1:] if '(' in i])
    sub[subject[:-1]] = lessens
print(sub)