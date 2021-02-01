import math

def fact(n):
    for i in range(n):
        if i > n:
            break
        yield  math.factorial(i+1)

for el in fact(5):
    print(el)