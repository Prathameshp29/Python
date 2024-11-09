def calculate_simple_interest(principal, rate, time):
    # Simple Interest formula
    simple_interest = (principal * rate * time) / 100
    return simple_interest

# Given values
principal_amount = 200  
rate_of_interest = 5   
time_period = 5         

# Calculate Simple Interest
simple_interest = calculate_simple_interest(principal_amount, rate_of_interest, time_period)

# Print the result
print(f"The Simple Interest on Rs. {principal_amount} for {time_period} years at {rate_of_interest}% per year is Rs. {simple_interest}.")