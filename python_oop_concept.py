# object oriented programming
# common topic in almost all popular programming languages(python,c++, java)
# with common idea but with different syntax
# oop is just a style/way to write a code
# very helpfull in creating real world programs
# we will see other advantages when we will start learning oop
# clas, object(instance), method

class Person:
    def __init__(self):
        pass

    def __init__(self, name = "", age = 0, address = ""):
        # instance variables
        self.name = name
        self.age = age
        self.address = address
    
    def information(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Address: {self.address}")


if __name__ == '__main__':
    p1 = Person()
    p1.name = "Shahed"
    p1.age = 18
    p1.address = "East Adalotpara, Tangail"
    p1.information()
