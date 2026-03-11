n=input("Enter the number to check if it is palindrom or not : ")
if n==n[::-1]:
    print(f"{n} is a palindrome number ")
else :
    print(f"{n} is not a palindrome number")