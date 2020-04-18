from python_oop_concept import Person,Laptop


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
