# The decimal number, 585 = 10010010012 (binary), is palindromic in both bases.

# Find the sum of all numbers, less than one million, which are palindromic in base 10 and base 2.

# (Please note that the palindromic number, in either base, may not include leading zeros.)

def is_palindromic(n):
	return str(n) == str(n)[::-1]

total = 0
for i in range(1_000_000):
	# bin(i)[2::] removes the leading "0b". e.g. 0b1011 becomes 1011
	if is_palindromic(i) and is_palindromic(bin(i)[2::]): total += i

print(total)