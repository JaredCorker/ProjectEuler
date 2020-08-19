# A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

# a^2 + b^2 = c^2
# For example, 3^2 + 4^2 = 9 + 16 = 25 = 5^2.

# There exists exactly one Pythagorean triplet for which a + b + c = 1000.
# Find the product abc.

def pythagorean_triplet():
    a = 1
    b = 2
    c = 1000 - (a + b)

    while (a < b < c):
        while (b < c):
            if a ** 2 + b ** 2 == c ** 2:
                d = a * b * c
                return (a, b, c, d)
            b += 1
            c = 1000 - (a + b)
        a += 1
        b = a + 1
        c = 1000 - (a + b)

print(pythagorean_triplet())