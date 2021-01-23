def degree(num,step):
    answer = 0
    step1 = num * num
    while step!=2:
        if num == 0:
            return  answer
        else:
            answer = step1*num
            step1 = answer
        step -=1
    return answer

print(degree(5,7))