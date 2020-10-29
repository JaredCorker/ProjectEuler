# The following iterative sequence is defined for the set of positive integers:

# n → n/2 (n is even)
# n → 3n + 1 (n is odd)

# Using the rule above and starting with 13, we generate the following sequence:

# 13 → 40 → 20 → 10 → 5 → 16 → 8 → 4 → 2 → 1
# It can be seen that this sequence (starting at 13 and finishing at 1) contains 10 terms. Although it has not been proved yet (Collatz Problem), it is thought that all starting numbers finish at 1.

# Which starting number, under one million, produces the longest chain?

# NOTE: Once the chain starts the terms are allowed to go above one million.

from tqdm import tqdm

def collatz(n):
    count = 0
    while n != 1:
        if n % 2 == 0:
            n = int(n / 2)
        else:
            n = (n * 3) + 1
        count += 1 
    return count

largest_count = 0
starting_number = 13
for i in tqdm(range(13, 1000001)):
    count = collatz(i)
    if count > largest_count:
        largest_count = count
        starting_number = i

print(largest_count, starting_number)
