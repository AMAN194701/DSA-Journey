# Starting with If-else 
# Q. Take age as input from the user and print the category

age =int(input("Enter your age : "))

if age <=12:
    print("Child")
elif age >=13 and age<18:
    print("Teenage")
elif age >=18 :
    print("You are an Adult ")
else :
    print("Invalid input ")