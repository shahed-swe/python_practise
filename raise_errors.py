def add(a,b):
    if (type(a) == int and type(b) == b):
        return a + b
    raise TypeError("Wrong Data Type has been passed")

# print(add('1','2'))

# raise errors example 1
# NotImplementedError
# abstract method

class Animal:
    def __init__(self, name):
        self.name = name

    def sound(self):
        raise NotImplementedError('you have to define this method in subclass')


class Dog(Animal):
    def __init__(self,name,breed):
        super().__init__(name)
        self.breed = breed
    
    def sound(self):
        return "Bhau Bhau"

class Cat(Animal):
    def __init__(self,name,breed):
        super().__init__(name)
        self.breed = breed
    
    def sound(self):
        return "Meaw Meaw"


doggy = Dog('doggy','pug')
cat = Cat('Cat','Meau')
print(doggy.sound())
print(cat.sound())
    

