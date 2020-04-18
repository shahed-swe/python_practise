# multi level inheritance


class Phone:
    discount_price = 10 #class variable has been declared
    count_instance = 0
    def __init__(self):
        pass

    def __init__(self, brand_name = None, model_name = None,price = 0):
        self.brand_name = brand_name
        self.model_name = model_name
        self._price = max(price, 0) #a simple trick
        # if price > 0:
        #     self._price = price
        # else:
        #     self._price = 0
        # self.complete_specification = f"{self.brand_name} {self.model_name} and Price {self._price}"

    @property    #get
    def price(self):
        return self._price

    @price.setter   #set
    def price(self,new_price):
        self._price = max(new_price, 0)


    @property
    def complete_specification(self):
        return f"{self.brand_name} {self.model_name} and Price {self._price}"

    def make_a_call(self, phone_number):
        print(f"Calling {phone_number} .....")

    def full_name(self):
        return f"{self.brand_name} {self.model_name}"


class Smartphone(Phone):
    discount_price = 10 #class variable has been declared
    count_instance = 0
    def __init__(self):
        pass

    def __init__(self, brand_name = None, model_name = None,price = 0, ram = None, internal_memory = None, rear_camera = None):
        # Phone.__init__(self, brand_name,model_name, price)
        # super().__init__(brand_name, model_name,price)
        super().__init__(brand_name = None, model_name = None,price = 0)
        self.ram = ram
        self.internal_memory = internal_memory
        self.rear_camera = rear_camera

    def full_name(self):
        return f"Name: {self.brand_name} {self.model_name}\nPrice: {self._price}\nInternal Memory: {self.internal_memory}"

class Flagship(Smartphone):
    def __init__(self):
        pass

    def __init__(self, brand_name = None, model_name = None,price = 0, ram = None, internal_memory = None, rear_camera = None,front_camera = None,Processor = None):
        super().__init__(brand_name = None, model_name = None,price = 0, ram = None, internal_memory = None, rear_camera = None)
        self.front_camera = front_camera
        self.processor = Processor


    def full_name(self):
        return f"Name: {self.brand_name} {self.model_name}\nPrice: {self._price}\nRam: {self.ram}\nFront Camera: {self.front_camera}\nRare Camera: {self.rear_camera}\nProcessor: {self.processor}"


# p1 = Phone()
# s1 = Smartphone('Nokia','Lumia 800',900000,'4gb','64gb','20mp')
# s1 = Smartphone()
s1 = Flagship()
s1.brand_name = "Nokia"
s1.model_name = "Lumia 900"
s1.price = 90000
s1.internal_memory = "64gb"
s1.front_camera = "24mp"
s1.rear_camera = "12mp"
s1.ram = "6gb"
s1.processor = "520 poly carbon"
print(s1.full_name())
print(s1.__dict__)
print(s1.full_name())
print(s1.complete_specification)


# print(help(Flagship))

# isinstance --> helps to check the object is for it;s class or not
print(isinstance(s1, Phone))
print(isinstance(s1, Smartphone))
print(isinstance(s1, Flagship))
s2 = Smartphone()
print(isinstance(s2, Phone))
print(isinstance(s2, Smartphone))
print(isinstance(s2, Flagship))
s3 = Phone()
print(isinstance(s3, Phone))
print(isinstance(s3, Smartphone))
print(isinstance(s3, Flagship))
# issubclass --> check the subclas
print(issubclass(Smartphone, Phone))
print(issubclass(Smartphone, Flagship))
print(issubclass(Flagship, Phone))
print(issubclass(Flagship, Smartphone))