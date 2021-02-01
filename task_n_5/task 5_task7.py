import json

dict_firm = {}
average = []

with open('task_7.txt') as f:
    lines = f.readlines()

for line in lines:
    name, format_com, rev, cost = line.split()
    prof = int(rev) - int(cost)
    dict_firm[name] = prof
    if prof > 0:
        average.append(prof)

average = sum(average) / len(average)

information = [dict_firm, {"average_profit": average}]

with open('task_7.json', 'w') as file:
    json.dump(information, file)

with open('task_7.json') as file:
    print(json.load(file))