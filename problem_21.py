# Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
# If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair and each of a and b are called amicable numbers.

# For example, the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore d(220) = 284. The proper divisors of 284 are 1, 2, 4, 71 and 142; so d(284) = 220.

# Evaluate the sum of all the amicable numbers under 10000.

import math
from tqdm import tqdm

def sum_factors(n):
    factors = [1]
    for i in range(2, int(math.sqrt(n) + 1)):
        if n % i == 0:
            factors.append(i)
            factors.append(n // i)
    return sum(factors)

def is_amicable(n):
    return n == sum_factors(sum_factors(n)) 

sum_amicable = 0
for i in tqdm(range(2, 10001)):
    if is_amicable(i):
        sum_amicable

print(sum_amicable)
