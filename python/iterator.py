from math import sqrt

class MyRange(object):

    def __init__(self, n):
        """Construct iterator."""
        self.n = n

    def __iter__(self):
        """Initialize iterator."""
        self.i = 0
        return self

    def __next__(self):
        if self.i < self.n:
            r = self.i
            self.i += 1
            return r
        else:
            raise StopIteration()

    def next(self):
        return self.__next__()


#  for i in MyRange(3):
    #  print(i)


def fibonacci(n):
    # proceed at yield() when function is called again
    # function with yield() generators iterator if __next__() method
    a = 0
    b = 1
    for i in range(n):
        c = a + b
        if i >= 1:
            a = b
            b = c
        yield c


#  for i in fibonacci(5):
    #  print(i)


def is_prime(x):
    p = True
    for k in range(2, int(sqrt(x)) + 1):
        if x % k == 0:
            p = False
            break
    return p

def primes(n):
    k = 2
    for i in range(n):
        k += 1
        while not is_prime(k):
            k += 1
        yield k


for i in primes(10):
    print(i)
