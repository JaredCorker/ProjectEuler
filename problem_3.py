#The prime factors of 13195 are 5, 7, 13 and 29.

#What is the largest prime factor of the number 600851475143 ?

def get_factors(n):
    factors = []
    if n % 2 == 0:
        for x in range (1, int(n / 2)):
            
    else:
        for x in range (1, int((n + 1) / 2)):
            print(x)

def is_prime(n):
    if n % 2 != 0 and n % 3 != 0 and n % 5 != 0:
        return True
    else:
        return False

def largest_prime(n):
    get_factors(n)

largest_prime(600851475143)