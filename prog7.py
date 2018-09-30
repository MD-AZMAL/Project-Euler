"""
Problem 7
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?
"""
from math import sqrt


def isprime(N):
    for i in range(2, int(sqrt(N)) + 1):
        if N % i == 0:
            return False
    return True

# for i in range(1,15):
# 	if isprime(i) is  True:
# 		print(i)


cnt = 1
start = 2

while cnt < 10001:
    start += 1
    if isprime(start):
        cnt += 1

print(start)
