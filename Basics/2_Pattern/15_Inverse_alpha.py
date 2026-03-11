# print("To print inverse Alphabet Triangle Pattern ")
n=int(input("Enter the number of rows : "))
for row in range(n,0,-1):           # Condition for row in decreasing order 
    for col in range(row):          # Con. for Printing alphabet
        print(chr(65+col), end="")  # printing no. of alphabet
    print()     
