"""
Starting in the top left corner of a 2×2 grid, and only being able to move to the right and down, there are exactly 6 routes to the bottom right corner.


How many such routes are there through a 20×20 grid?
"""


def factorial(n):
    fact = 1
    for i in range(1, n + 1):
        fact *= i
    return fact


nRoutes = factorial(2 * 20) // (factorial(20) * factorial(20))

print(nRoutes)
