n=int(input("Enter the number for which you want to check if it is prime or not : "))
is_prime=True
if n==1:
    print(f"{n} is neither prime nor composite ")
elif n>1:
    for num in range(2,n):
        if n%num==0:
            is_prime=False
            break
if is_prime:
    print(f"{n} is a prime number ")
else :
    print(f"{n} is not a prime number ")