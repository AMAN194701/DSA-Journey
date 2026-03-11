print("To print the number pyramid ")
n=int(input("Enter the number of rows u want to print "))

for row in range(1,n+1):  #condition for number of rows
    for num in range(1,row+1): # condition for first half 
        print(num, end="")

    
    for space in range((n*2)-(row*2)):  #condition for space
        print( " ", end="")
    

    for num in range(row,0,-1): #condition for 2nd half
        print(num, end="")
    print()
    

