"""
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

a^2 + b^2 = c^2
For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
"""

from math import sqrt

sum = 1000

for i in range(1, 1001):
    for j in range(i + 1, 1001):
        sqr = sqrt(i * i + j * j)
        if i + j + sqr == 1000:
            print(i * j * int(sqr))
