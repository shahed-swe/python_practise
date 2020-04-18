from python_oop_concept import *
import class_variable as cv

if __name__ == '__main__':
    # p1 = Person()
    # p1.name = "Shahed"
    # p1.age = 18
    # # p1.address = "East Adalotpara, Tangail"
    # p1.information()

    l1 = Laptop()
    l1.brand_name = "Hp"
    l1.model_name = "Notebook"
    l1.price = 47000
    laptop_info = l1.laptop_information()
    laptop_price = l1.laptop_price()
    print("{}\nPrice: {}".format(laptop_info,laptop_price))
    # print(l1.number(50,10000000000000))
    # take = list(l1.number(50,1000))
    # for i in take:
    #     print(i)
    c1 = Calculator()
    c1.number1 = 3
    list2 = c1.is_even(1,2,3,4,5,6)
    print(list2)
    list2 = [3,1,5,6,2,14]
    c1.sort_list(list2)
    print(list2)
    new_laptop = cv.Laptop()
    new_laptop.brand_name = "Hp Probook"
    new_laptop.model_name = "450 G6 core i7 9th Generation"
    new_laptop.price = int(input("Enter laptop price:"))
    print("{}\nPrice After Discount: {}".format(new_laptop.laptop_details(),new_laptop.apply_discount()))
    
