#The sum of the squares of the first ten natural numbers is,
#   1*1 + 2*2 + ... + 10*10 = 385
#The square of the sum of the first ten natural numbers is,
#   (1 + 2 + 3 +... + 10)^2 = 55^2 = 3025
#Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is .
#   3025 - 385 = 2640
#Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.

def sum_of_squares():
    sum_of_squares = 0
    for x in range(1, 101):
        sum_of_squares += x ** 2
    return sum_of_squares

def square_of_the_sum():
    sum_of_numbers = 0
    for x in range(1, 101):
        sum_of_numbers += x
    square_of_the_sum = sum_of_numbers ** 2
    return square_of_the_sum

print(square_of_the_sum() - sum_of_squares())