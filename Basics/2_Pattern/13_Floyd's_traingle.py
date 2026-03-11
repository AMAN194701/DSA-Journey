print("To print Floyed Triangle ")
number=1
n=int(input("Enter the number of rows : "))
for row in range(1,n+1):                    # condition for rows
    for col in range(1,row+1):              # printing the number equal to current row no.
        print(number," ", end="")           # printing the number in same line
        number=number+1                     # updating the number 
    print()                                 # nxt line