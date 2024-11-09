def sum_natural_numbers_loop(n):
    total = 0
    for i in range(1, n + 1):
        total += i
    return total
n = 10
print("Sum of numbers:", sum_natural_numbers_loop(n))