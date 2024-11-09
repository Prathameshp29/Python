def check_voting_eligibility(age):
    if age >= 18:
        return "You are eligible to vote."
    else:
        return "You are not eligible to vote."

# Take input from the user
try:
    age = int(input("Enter your age: "))  # Convert input to an integer

    # Check and print eligibility
    eligibility_message = check_voting_eligibility(age)
    print(eligibility_message)

except ValueError:
    print("Please enter a valid age.")