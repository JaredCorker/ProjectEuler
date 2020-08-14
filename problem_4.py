#A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

#Find the largest palindrome made from the product of two 3-digit numbers.

import math

def get_3_digit_factors(n):
    factors = []
    for x in range(100, int(math.sqrt(n) + 1)):
        if n % x == 0:
            if len(str(x)) == 3 and len(str(n // x)) == 3:
                factors.append(x)
                factors.append(n // x)
    return factors

def is_palindrome(n):
    n = str(n)
    if len(n) <= 1:
        return True

    if n[0] != n[len(n) - 1]:
        return False

    stripped = n[1 : len(n) - 1]
    return is_palindrome(stripped)

def find_palindromes():
    # highest possible product of two 3-digit numbers (900 * 900 = 998001)
    x = 998001
    # stop at lowest possible product of two 3-digit numbers (100 * 100 = 10000)
    while (x > 9999):
        if is_palindrome(x):
            if len(get_3_digit_factors(x)) > 0:
                return x
        x -= 1

print(find_palindromes())