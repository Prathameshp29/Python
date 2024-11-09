num1 = input("Enter the first number: ")
num2 = input("Enter the second number: ")

# Print the original numbers
print(f"Before swapping: num1 = {num1}, num2 = {num2}")

# Swap the numbers using a temporary variable
temp = num1
num1 = num2
num2 = temp

# Print the swapped numbers
print(f"After swapping: num1 = {num1}, num2 = {num2}")