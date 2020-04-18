import math as m
class Circle:
    pi = m.pi #this is an instance variable

    def __init__(self, radius):
        self.radius = radius

    def circle_circum(self):
        return 2*Circle.pi*self.radius #to use class variable we have to write exact name of the class



class Laptop:
    discount_price = 10 #class variable has been declared
    count_instance = 0
    def __init__(self):
        Laptop.count_instance += 1
        pass

    def __inti__(self, brand_name = None, model_name = None,price = None):
        Laptop.count_instance += 1
        self.brand_name = brand_name
        self.model_name = model_name
        self.price = price
    
    def laptop_details(self):
        return f"Laptop Name: {self.brand_name}\nModel Name: {self.model_name}"

    def apply_discount(self):
        # self.price
        off_price = (Laptop.discount_price/100)*self.price
        return self.price - off_price


if __name__ == '__main__':
    Laptop.discount_price = 10 #this will not make any new instance variable and only will use (discount_price) as class variable
    new_laptop = Laptop()
    new_laptop.brand_name = "Dell Notebook"
    new_laptop.model_name = "Vostro 1016"
    new_laptop.price = 46000
    print(new_laptop.laptop_details())
    print("Laptop Price {}".format(new_laptop.apply_discount()))
    print(new_laptop.__dict__)
    # now we will convert our class variable to instance variable
    new_laptop.discount_price = 20
    print(new_laptop.__dict__)
    new_laptop2 = Laptop()
    new_laptop3 = Laptop()
    print(Laptop.count_instance)
    print(new_laptop3.count_instance)