import math
from sys import maxsize

# a: [-999, 999] -> range(-999, 1000)
# b: [-1000, 1000] -> range(-1000, 1001)

def main():
    #print(list(filter(is_prime, range(100))))
    max = 0
    for a in range(-999, 1000):
        for b in range(-1000, 1001):
            n = check_primes(formula(a, b))
            if n > max:
                max = n
                res = (a, b)
                print(f"!!!!!!!!!!!!!!!!!!!!!  {max}  !!!!!!!!!!!!!!!!!!!!!!")
        #print(f"a: {a}")

    print(res)
    

def check_primes(f):
    for i in range(maxsize):
        res = f(i)
        prime = is_prime(res)
        if(not prime):
            return i


def formula(a, b):
    return lambda n: n**2 + a*n + b


def f(n):
     return n**2 + n + 41

def factors(n):
    k = range(1, math.ceil(math.sqrt(abs(n)))+1)
    k = list(map(lambda x : (n/x, x), k))
    k = list(filter(lambda x: x[0]%1 == 0, k))
    k = set([x for fs in k for x in fs])
    return k

# def is_prime(n):
#    if n == 0: return True
#    return len(factors(n)) <= 2

def is_prime(n):
    for i in range(2, math.ceil(math.sqrt(abs(n)))+1):
        if n%i == 0 :
            return False
    return True



class Number:
    
    def __init__(self, val):
        self.val = val
        self.find_factors()

    def find_factors():
        k = range(1, math.ceil(math.sqrt(abs(self.val)))+1)
        k = list(map(lambda x : (n/x, x), k))
        k = list(filter(lambda x: x[0]%1 == 0, k))
        k = set([x for fs in k for x in fs])
        self.factors = list(k)




if __name__ == '__main__':
    main()