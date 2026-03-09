print("To print Half diamond patter")
n=int(input("Enter the number of rows : "))
for row in range(1,n+1):    
    for star in range(row):     
        print("*", end="")
    print()

for row in range(1,n+1):
    for star in range(n-row+1):
        print("*",end="")
    print()


# Output
# for n=5 

# *
# **
# ***
# ****
# *****
# *****
# ****
# ***
# **
# *