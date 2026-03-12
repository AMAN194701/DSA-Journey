n=int(input("Enter the number : "))
def rev(n):
    if n==0:
        return
    print(n, end=" ")
    rev(n-1)
rev(n)