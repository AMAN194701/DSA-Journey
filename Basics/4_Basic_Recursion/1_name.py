name=input("Enter your name : ")
n=int(input("How many times do you want your name to be printed : "))
def number( n,name):
    if n==0 :
        return
    print(name)
    number(n-1,name)
    
number(n,name)
