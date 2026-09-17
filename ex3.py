from functools import reduce

#3.1

def is_armstrong(n):
    k = len(str(n))
    return reduce(lambda x, y: x + pow(int(y),k), str(n), 0) == n


#3.2

def armstrong_range(n1,n2):
    return list(filter(is_armstrong, range(n1,n2+1)))

if __name__ == '__main__':
    n1 = input('Enter a number: ')
    if not n1.isdigit():
        print('invalid input')
        exit(1)
    n2 = input('Enter another number: ')
    if not n2.isdigit():
        print('invalid input')
        exit(1)

    print(armstrong_range(int(n1),int(n2)))
