print("To print inverse Alphabet Triangle Pattern ")
n=int(input("Enter the number of rows : "))
for row in range(n,0,-1):
    for col in range(row):
        print(chr(65+col), end="")
    print()