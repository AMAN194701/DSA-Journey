print("To print binary Traingle ")
n=int(input("Enter the number of rows : "))
for row in range(1,n+1):

    if row%2==0: # observation how binary changes
        num=0
    else :
        num=1
    
    for binary in range(1, row+1):
        print(num, end=" ") # printing binary digits

        num=1-num # Flipping the number

    print() #next line