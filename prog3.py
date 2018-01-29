"""
Problem 3 
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
"""

"""
the largest prime factor will lie between 2 and sqrt(of number) by sieve of eratosthenes
hence loop from 2 to sqrt(n) check in each iteration that iterative value is both prime and a factor of n
last iterating value is the largest prime factor 
"""


from math import sqrt

gigantic_number = 600851475143

def isprime(n):
	for i in range(2,int(sqrt(n))+1):
		if n%i == 0:
			return False
	return True

for i in range(2,int(sqrt(gigantic_number)) +1):
	if isprime(i) and gigantic_number%i == 0:
		largest = i
print(largest)
