#The prime factors of 13195 are 5, 7, 13 and 29.

#What is the largest prime factor of the number 600851475143 ?

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

def largest_prime(n):
    factors = get_factors(n)
    largest_prime = 0
    for x in factors:
        if is_prime(x) and x > largest_prime:
            largest_prime = x
    return largest_prime

print(largest_prime(600851475143))