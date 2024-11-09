num = int(input("Enter a positive number: "))

factorial = 1
original_num = num

while num > 1:
        factorial *= num
        num -= 1
print(f"The factorial of {original_num} is: {factorial}")
