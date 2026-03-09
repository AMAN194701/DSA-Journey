print("To print Alphabet Tringle Patter ")
n= int(input("Enter the number of row : ")) 
for row in range(n):                    # condtion for no. of rows
    for col in range(row+1):            # condn for printing alphabet equal to current row no
        print(chr(65+col), end="")      # Printing Alphabet in same line
    print()                             # next line