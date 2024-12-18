class Average:
    def __init__(self, num1, num2, num3):
        self.num1 = num1
        self.num2 = num2
        self.num3 = num3 

    def calculate_average(self):
        return (self.num1 + self.num2 + self.num3) / 3


# Creating an object of the class
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
num3 = float(input("Enter the third number: "))

avg = Average(num1, num2, num3)
print(f"Average: {avg.calculate_average()}")
