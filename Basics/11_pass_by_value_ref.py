# Pass by value => when copy is passed
# Pass by reference => when the actual value is passed 

# Imp:  Python exactly do not uses pass by value or ref but insted it uses pass by object refrence 
# i.e object refrence is passed and its behaviour depend on mutable and immutability

# 1) Immutable Objects (behave like pass-by-value)
# eg int, float, string , tuple

def immutable(a):
    a = a + 40

x = 10
immutable(x)
print(x)

# 2)  Mutable Objects (behave like pass-by-reference)
# eg set , dict, list
def mutable(lst):
    lst.append(10)

nums=[3,2,5]
mutable(nums)
print(nums)