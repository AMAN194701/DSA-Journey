# find the factorial of a number 
n=int(input("Enter the number for which u want to find the factorial : "))
num=n
fact=1
while n >1:
    fact*=n
    n-=1
print(f"The factorial of {num} is {fact}")


# or 
# for i in range(1,n+1):
#     fact*=i
# print(fact)