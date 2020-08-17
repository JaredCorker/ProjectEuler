# The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

# Find the sum of all the primes below two million.

import math
import time
from tqdm import tqdm

start_time = time.time()

def get_factors(n):
    factors = []
    for x in range(1, int(math.sqrt(n) + 1)):
        if n % x == 0:
            factors.append(x)
            factors.append(n // x)
    return factors

def is_prime(n):
    return len(get_factors(n)) == 2

# Skips all even numbers, takes ~50 seconds

# def sum_of_primes(n):
#     primes_sum = 0
#     if n > 2:
#         primes_sum += 2
#         for x in tqdm(range(3, n, 2)):
#             if is_prime(x):
#                 primes_sum += x
#     return primes_sum

# Skips all even numbers but skips divisibles of 5 as well, takes ~ 40 seconds
# (start at 5 so initial 5 isnt skipped, all other multiples of 5 can be skipped)
# eg 5 -> 7 -> 9 -> 11 -> 13 -> 17 -> 19

def sum_of_primes(n):
    primes_sum = 0
    if n > 2:
        primes_sum += 2
        if n > 3:
            primes_sum += 3
            i = 5
            while (i < n):
                if is_prime(i):
                    primes_sum += i
                if i % 10 == 3:
                    i += 4
                else:
                    i += 2
    return primes_sum
    
print(sum_of_primes(2000000))

print("%.2f seconds" % (time.time() - start_time))