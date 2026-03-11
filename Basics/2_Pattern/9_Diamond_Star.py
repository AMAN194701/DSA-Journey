print("To print the Diamond star pattern ")
n=int(input("Enter the number of rows u want : "))
for row in range(1,n+1):
    for space in range(n-row):
        print(" ",end="")

    for star in range(2*row-1):
        print("*",end="")
    print()

for row in range(1,n+1):
    for space in range(row-1):
        print(" ",end="")
    for star in range(2*(n-row)+1):
        print("*", end="")
    print()
