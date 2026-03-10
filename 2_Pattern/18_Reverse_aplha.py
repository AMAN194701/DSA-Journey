n=int(input("Enter the number of row you want : "))
for row in range(1,n+1):
    for col in range(row):
        print(chr(65+(n-row)+col), end="")
    print()


# Output :-
# E
# DE
# CDE
# BCDE
# ABCDE