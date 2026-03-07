print("To print Invert Right triangle star pattern : ")
n =int(input("Enter the number of Rows : "))
for row in range(n,0,-1):
    for col in range(row):
        print("*" , end="")
    print()