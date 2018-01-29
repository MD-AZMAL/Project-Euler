"""
Problem 5 
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
"""

"""
number divisible from 1 - 20 must be a factor of 2520...which is divisible from each number between 1-10
hence check for divisibility of number from 11 to 20 starting from 2520
"""

def isdivisible(n):
	for i in range(11,21):
		if n%i != 0:
			return False
	return True

num = 2520

while isdivisible(num) == False:
	num += 2520
	
print(num)
	
# works good on the given test case but is not robust ..... cannot be scaled for cases like evenly devisible by nos b/w 1 - n

