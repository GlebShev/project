import functools
def my_func(el0, el_next):
    return el0 * el_next

my_list = [i for i in range(99, 1001) if i%2 == 0]
answer = [functools.reduce(my_func, [i for i in my_list])]
print(answer)