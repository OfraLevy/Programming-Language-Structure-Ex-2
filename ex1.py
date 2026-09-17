#1.0
from functools import reduce
from time import perf_counter

f = lambda x: x/2 +2

#1.1
def high_func(f,l):
    return [f(x) for x in l ]
lst = high_func(f,range(10001))

#1.2 , 1.3
start = perf_counter()

total1 = sum(lst)

end = perf_counter()
print("functional time: " )
print ( end - start)
print("sum with two high functions: ")
print (total1)

#imperative
start = perf_counter()

total2 = 0
for x in lst:
    total2 = total2 + x

end = perf_counter()
print("imperative time: " )
print ( end - start)
print("sum with imperative method: ")
print (total2)

#1.4
def high_func2(f,l):
    return reduce(lambda total, current : total + f(current), l, 0)
total3 = high_func2(f,range(10001))
print("sum with one high function: ")
print (total3)

