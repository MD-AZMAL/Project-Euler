"""
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
"""
from math import sqrt


def isprime(n):
    for i in range(2, int(sqrt(n)) + 1):
        if n % i == 0:
            return 0
    return n


s = 0
for i in range(2, 2000000):
    s += isprime(i)

print(s)
