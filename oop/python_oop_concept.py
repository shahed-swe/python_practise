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

    def __init__(self, name = None, age = None, address = None):
        # instance variables
        self.name = name
        self.age = age
        self.address = address
    
    def information(self):
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Address: {self.address}")


class Laptop:
    def __init__(self):
        pass

    def __init__(self, brand_name = None, model_name = None, price = None):
        self.brand_name = brand_name
        self.model_name = model_name
        self.price = price

    def laptop_information(self):
        return "Brand name: {}\nModel name: {}".format(self.brand_name,self.model_name)
    
    def laptop_price(self):
        percent = 0.2
        return self.price + (self.price*percent)
    
    # @staticmethod
    # async def number(delay, to):
    #     '''yield numbers from zero to *to* every *delay* second.'''
    #     for i in range(to):
    #         yield i
    #         await asyncio.sleep(delay)