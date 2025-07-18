# This program calculates the sum of the first n natural numbers.
def sum_of_first_n_numbers():
    n = int(input("Enter a positive integer: "))
    sum = 0
    while True:
        sum = sum + n
        n -= 1
        if n == 0:
            break

    print(sum)


sum_of_first_n_numbers()