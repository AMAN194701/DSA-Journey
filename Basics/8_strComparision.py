# String Comparison using equality operator
class solution:
    def equl(self, str1, str2):
        if str1==str2:
            print("String are equal ")
        else: 
            print("String are not equal ")

if __name__=="__main__":
    obj=solution()
    obj.equl("user1","user2")
    obj.equl("user1","user1")