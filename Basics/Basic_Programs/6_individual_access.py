# access the individual element of the string

class sol:
    def element(self, word):
        for i in range(len(word)):
            print(word[i])

if __name__=="__main__":
    obj= sol()
obj.element("user")