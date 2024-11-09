def find_max(num1, num2):
    if num1 > num2:
        return num1
    else:
        return num2

# Input from the user
number1 = float(input("Enter the first number: "))
number2 = float(input("Enter the second number: "))

maximum = find_max(number1, number2)
print(f"The maximum of {number1} and {number2} is {maximum}")
