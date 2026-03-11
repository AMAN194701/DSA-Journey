n=int(input("Enter the number of rows u want : "))
for row in range(n):                    # For Rows
    for col in range((row+1)):          # controls number of characters in each row
        print(chr(65+row),end="")
    print()
    
    