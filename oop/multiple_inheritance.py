class A:
    def class_a_method(self):
        return "I'am Class A method"
    
    def hello(self):
        return "Hello i am class A"

class B:
    def class_a_method(self):
        return "I'am Class B method"
    
    def hello(self):
        return "Hello i am class B"

    
class C(A,B):
    pass



c1 = C()

print(c1.hello())
print(C.mro())
print(help(c1))