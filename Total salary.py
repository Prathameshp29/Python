def calculate_average(num1, num2, num3):
    average = (num1 + num2 + num3) / 3
    return average

def calculate_total_salary(salary):
    hra = 0.10 * salary  # 10% HRA
    ta = 0.05 * salary   # 5% TA
    total_salary = salary + hra + ta
    return total_salary

# Main part of the program
if __name__ == "__main__":
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    num3 = float(input("Enter the third number: "))

    salary = float(input("Enter your salary: "))

    average = calculate_average(num1, num2, num3)
    print(f"The average of the three numbers is: {average:.2f}")

    total_salary = calculate_total_salary(salary)
    print(f"Your total salary after adding HRA and TA is: {total_salary:.2f}")
