class SimpleInterest:
    def __init__(self, principal, rate, time):
        self.principal = principal
        self.rate = rate
        self.time = time

    def calculate_interest(self):
        return (self.principal * self.rate * self.time) / 100


# Creating an object of the class
principal = float(input("Enter the principal amount: "))
rate = float(input("Enter the rate of interest: "))
time = float(input("Enter the time (in years): "))

si = SimpleInterest(principal, rate, time)  
print(f"Simple Interest: {si.calculate_interest()}")
