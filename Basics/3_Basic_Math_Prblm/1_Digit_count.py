n=int(input("Enter multiple number of digit : "))
temp=n
count=0
while temp>0:
    temp=temp//10
    count+=1
print(f"The number {n} has {count} digit")
