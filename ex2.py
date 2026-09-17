#2.0
from functools import reduce

numbers = list(range(1, 1001))

even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
odd_numbers = list(filter(lambda x: x % 2 != 0, numbers))

#2.1

def mult_even(ev_num):
    return reduce(lambda x, y: x * y, ev_num)

def op_odd(odd_num):
    f = lambda x: x / 2 + 2
    return reduce(lambda x, y: f(x) + y, odd_num)

#2.2

print(mult_even(even_numbers))
print(op_odd(odd_numbers))
