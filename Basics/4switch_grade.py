# Switch case using in grading

grade=input("Enter your grade : ")
match grade:
    case "A":
        print("Excellent")
    case "B":
        print("Good")
    case "C":
        print("U can do better")
    case _:
        print("Not defined")