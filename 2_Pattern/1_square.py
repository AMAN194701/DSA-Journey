print("To print Star square ")
n =int(input("Enter the number of rows/Col for square : "))
for row in range(1,n+1):
    for col in range(n):
        print(" * ", end= "")
    print()
