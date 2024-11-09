def can_vote(age):
    if age >= 18:
        return "You are eligible to vote."
    else:
        return "You are not eligible to vote."

# Input from the user
age = int(input("Enter your age: "))

result = can_vote(age)
print(result)
