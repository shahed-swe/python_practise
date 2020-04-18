# special magic methods / dunder methods
# operator overloading
# polymorphism


class Phone:
    def __init__(self):
        pass

    def __init__(self, brand=None, model=None, price=0):
        self.brand = brand
        self.model = model
        self.price = max(price,0)

    def phone_details(self):
        return f"{self.brand} {self.model}\nPrice {self.price}"

    def __str__(self):
        '''we should use __str__ to return a complete finist string'''
        return f"{self.brand} {self.model}"

    def __repr__(self):
        '''we should use repr to return object type thing like below'''
        return f"Phone('{self.brand}','{self.model}',{self.price})"

    def __len__(self):
        return len(self.phone_details())


    # operator overloading
    def __add__(self, other):
        return self.price + other.price



# https://docs.python.org/3.6/reference/datamodel.html
if __name__ == '__main__':
    p1 = Phone()
    p1.brand = "Nokia"
    p1.model = "Lumia 10"
    p1.price = 90000
    print(p1)
    print(str(p1))
    print(repr(p1))
    print(len(p1))
    print(p1.__repr__()) #another method to call representation dundar method
    # print(p1.__repr__().__doc__)
    p2 = Phone()
    p2.price = 45000
    p2.brand = "Xiaomi"
    p2.model = "Note 8"
    print(p2.__repr__())
    print(p1+p2) #here we have overloading operator