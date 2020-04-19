def add(a,b):
    if (type(a) == int and type(b) == b):
        return a + b
    raise TypeError("Wrong Data Type has been passed")

# print(add('1','2'))

# raise errors example 1
# NotImplementedError
# abstract method


# example - 1
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


# doggy = Dog('doggy','pug')
# cat = Cat('Cat','Meau')
# print(doggy.sound())
# print(cat.sound())


class Mobile:
    def __init__(self,name):
        self.name = name
    
class MobileStore:
    def __init__(self):
        self.mobiles = []

    def add_mobile(self,new_mobile):
        if isinstance(new_mobile, Mobile):
            self.mobiles.append(new_mobile)
        else:
            raise TypeError('new mobile should be object of mobile class ')


m1 = Mobile('one plus 6')
samsung = 'samsung galaxy s8'

mobostoer = MobileStore()
# print(mobostoer.mobiles)
mobostoer.add_mobile(m1)
mobo_phones = mobostoer.mobiles
# print(mobostoer.mobiles)
print(mobo_phones[0].name)


