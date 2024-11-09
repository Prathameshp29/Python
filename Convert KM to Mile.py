def kilometers_to_miles(kilometers):
    miles = kilometers * 0.621371  # 1 kilometer is approximately 0.621371 miles
    return miles

kilometers = float(input("Enter the distance in kilometers: "))

# Convert kilometers to miles
miles = kilometers_to_miles(kilometers)

# Print the result
print(f"{kilometers} kilometers is equal to {miles:.2f} miles.")