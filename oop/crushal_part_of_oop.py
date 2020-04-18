# Encapsulation
# Abstraction
# Some special naming convention
# Name Mangling

class Phone:
    discount_price = 10 #class variable has been declared
    count_instance = 0
    def __init__(self):
        Phone.count_instance += 1
        pass

    def __init__(self, brand_name = None, model_name = None,price = None):
        Phone.count_instance += 1
        self.brand_name = brand_name
        self.model_name = model_name
        self.price = price

    # defining class method
    @classmethod
    def count_instances(cls): #this is class method
        return "you have created {} instances".format(cls.count_instance)
    

    # @classmethod
    # def from_string(cls, string): #constructor using class method
    #     first,last,end = string.split(',')
    #     # price = int(price)
    #     return cls(first,last,end)

    def laptop_details(self): #instance methods
        return f"Phone Name: {self.brand_name}\nModel Name: {self.model_name}"

    def apply_discount(self): #instance methods
        # self.price
        off_price = (Phone.discount_price/100)*self.price
        return self.price - off_price

    @staticmethod
    def method_static():
        print("Static method has been called")

# _name #convention of private instance property/name
# __name__ #dunder /magic methods

# phone1 = Phone('Xiaommi','Redmi Note 7','20000')
# print(phone1.__dict__)




class NewPhone:
    discount_price = 10 #class variable has been declared
    count_instance = 0
    def __init__(self):
        NewPhone.count_instance += 1
        pass

    def __init__(self, brand_name = None, model_name = None,price = None):
        NewPhone.count_instance += 1
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



phone1 = NewPhone('Nokia','1100',1000)
print(phone1.brand_name)
print(phone1.model_name)
print(phone1.price)
phone1.price = 500
print(phone1.price)
print(phone1.complete_specification)
