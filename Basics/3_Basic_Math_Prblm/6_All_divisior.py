
class solution:
    def divisor(self, n):
        div_values=[]
        for num in range(2,n+1):
            if n%num==0:
                div_values.append(num)
        return div_values

d=solution()
n=int(input("Enter the number : "))
print(f"The divisor of {n} are :",end=" ")
print(d.divisor(n))