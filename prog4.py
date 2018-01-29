"""
Problem 4 
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
"""

"""
for each result of multiplication of each 3-digit number if it is palindrome then check if it is max_ or not
then return max
"""

def retPal(n):
	n = str(n)
	if n[::-1] == n:
		return True
	return False


def max_pal():	
	max_=0
	for i in range(999,99,-1):
		for j in range(999,99,-1):
			res = i*j
			if retPal(res) is True:
				if max_ < res:
					max_ = res
	return max_


print(max_pal())
