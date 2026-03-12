n=int(input("Enter the number till where u want to print all the number : "))
# class sol :
def number(n):
    if n==0:
        return
    number(n-1)
    print(n,end=" ")
    
number(n)