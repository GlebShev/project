import itertools

for i in itertools.count(3):
    if i> 10:
        break
    else:
        print(i)

my_cycle_list = [1, True, None, False, 1.4, "Hi"]
count = 0
for i in itertools.cycle(my_cycle_list):
    if count>10:
        break
    print(i)
    count +=1
