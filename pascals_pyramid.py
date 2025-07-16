def pascal_triangle(n):
    for i in range(n):
        # Printing spaces for alignment
        print(' '*(n-i), end='')

        num = 1
        for j in range(i+1):
            print(num, end=' ')
            num = num * (i - j) // (j + 1)
        print()

# Example usage
pascal_triangle(7)
