n = int(input("Enter the number of terms: "))

a, b = 0, 1
count = 0

print("Fibonacci series up to", n, "terms:")
while count < n:
    print(a, end=" ")
    a, b = b, a + b  
    count += 1
