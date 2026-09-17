from functools import reduce
from math import factorial


def power_function(n):
    def power(x):
        return x ** n
    return power

def map_power(n):
    return map(power_function, range(n))

def taylor(x, n):
    return reduce(
        lambda total, term: total + term,
        map(
            lambda f, power: f(x) / factorial(power),
            map_power(n),
            range(n)
        ),
        0
    )

if __name__ == '__main__':
    n = int(input("Enter number of powers:"))
    result = map_power(n)
    print(type(result))
    base = int(input("Enter base:"))
    print(reduce(lambda total, f: total+(f(base),),list(result),()))

