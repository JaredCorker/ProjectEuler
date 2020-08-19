# By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

# What is the 10 001st prime number?

import math

def get_factors(n):
    factors = []
    for x in range(1, int(math.sqrt(n) + 1)):
        if n % x == 0:
            factors.append(x)
            factors.append(n // x)
    return factors

def is_prime(n):
    return len(get_factors(n)) == 2

prime_numbers = []
i = 2
while (len(prime_numbers) < 10001):
    if (is_prime(i)):
        prime_numbers.append(i)
    i += 1

print(prime_numbers[10000])