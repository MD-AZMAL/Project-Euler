"""
Problem 1
If we list all the natural numbers below 10 that are multiples of 3 or 5, we get 3, 5, 6 and 9. The sum of these multiples is 23.

Find the sum of all the multiples of 3 or 5 below 1000.
"""

"""
take two loops that go from 0 to limit incrementing by 3 and 5 respectively add each iterating value to sum
"""

s = 0
lim = 1000

for i in range(0,lim,3):
	s += i

for i in range(0,lim,5):
	s += i

print(s)