n=int(input("Enter a number"))
temp=n;
rev=0
while(n>0):
    rem=n%10
    rev=rev*10+rem
    n=n//10
print("The reverse is",rev)
if(temp==rev):
    print("The number is palindrome",temp)
else:
    print("The number is not palindrome")
