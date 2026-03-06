# # Passing, Returning, and Assigning Strings
class solution:
    def modify(self, n):
        org=n
        org+=" Of user "
        return org 
    
if __name__=="__main__":
    obj = solution()
    x="Name"
    value = obj.modify(x)
    print("Original value : ", x)
    print("Modified value: ", value)

def modify (n):
    org = n 
    org+=" World"
    return org 

str="hello"
result= modify(str)
print("Original : ", str)
print("Modified: " ,result)
