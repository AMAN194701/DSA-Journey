print("To find the GDC of two number ")
n1=int(input("Enter the first number : "))
n2=int(input("Enter the second number : "))
cmm1=[]
for i in range(1,n1+1):
    if n1%i==0:
        cmm1.append(i)

cmm2=[]
for i in range(1,n2+1):
    if n2%i==0:
        cmm2.append(i)
print("Divisor of n1 are : ",cmm1)
print("Divisor of n2 are : ",cmm2)

common=[]
for num in cmm1:
    if num in cmm2:
        common.append(num)
print(f"The GDC of {n1} and {n2} is {max(common)}")