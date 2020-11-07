# n! means n × (n − 1) × ... × 3 × 2 × 1

# For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,
# and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.

# Find the sum of the digits in the number 100!
    
def factorial(n):
    product = n
    for i in range(n-1, 0, -1):
        product *= i

    return product

def sum_digits(n):
    return sum([int(x) for x in str(n)])

print(sum_digits(factorial(100)))
