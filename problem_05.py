#2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

#What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?

import time

start_time = time.time()

def is_factor(n, m):
    return n % m == 0

def factors_1_to_20():
    number_not_found = True
    i = 20
    while (number_not_found):
        if is_factor(i, 20) and is_factor(i, 19) and is_factor(i, 18) and is_factor(i, 17) and is_factor(i, 16) and is_factor(i, 15) and is_factor(i, 14) and is_factor(i, 13) and is_factor(i, 12) and is_factor(i, 11):
            return i
        i += 1

print(factors_1_to_20())

print("%.2f seconds" % (time.time() - start_time))