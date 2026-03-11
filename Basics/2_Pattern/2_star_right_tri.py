# Take input from the user and print the Right star pattern
print("To print Right Triangle star pattern ")
n=int(input("Enter the number of rows : "))
for row in range (1,n+1):
    for col in range(row):
        print("*",end="")
    print()
