n=5
# upper half
for row in range(1,n+1):
    for str in range(row):
        print("*",end="")

    for space in range(n*2-(row*2)):
        print(" ",end="")
    
    for str in range(row):
        print("*",end="")
    print()

# Lower half
for row in range(1,n):
    for str in range(n-row):
        print("*",end="")
    
    for space in range(row*2):
        print(" ",end="")

    for str in range(n-row):
        print("*",end="")
    print()


# Output : 

# *        *
# **      **
# ***    ***
# ****  ****
# **********
# ****  ****
# ***    ***
# **      **
# *        *
