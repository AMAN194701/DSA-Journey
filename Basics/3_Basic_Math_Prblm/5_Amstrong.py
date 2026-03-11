n=(input("Enter the number : "))
numint=int(n)
power=len(n)
sum=0
for num in n:
    digit=int(num)
    sum=sum+(digit**power)
if numint==sum:
    print("Amstrong ")
else :
    print("Not a amstrong number ")