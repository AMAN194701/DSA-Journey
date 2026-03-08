print("To Print the invert pyramid star ")
n =int(input("Enter the number of rows u want to print : "))
for row in range(1,n+1):
    for space in range(row-1):
        print(" ", end="")
    
    for star in range(2*(n-row)+1):
        print("*", end="")
    print()

