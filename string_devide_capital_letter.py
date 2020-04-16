def first_div(string):
    new_string = []
    make = []
    count1 = 0
    count2 = 0
    for i in range(len(string)):
        if string[i] == string[i].upper(): #this line of code will find the upper case letter
            count2 = i
            new_string = [string[j] for j in range(count1,count2)] #this will devide string like this exp: shahed to [s,h,a,h,e,d]
            make.append(''.join(new_string)) #this portion of code will make them like this [s,h,a,h,e,d] to shahed
            count1 = count2
    return make

def second_div(list1, string):
    new_string = []
    make = []
    new_list = ''.join(list1) #this is the same concept like before
    for i in range(len(string)):
        new_string = [string[i] for i in range(len(new_list), len(string))] #this will also make the same like this
        make = ''.join(new_string) #same
    return make

if __name__ == '__main__':
    string = input("Enter a string:") #getting string input
    hello = first_div(string)
    for i in hello:
        print(i)
    print(second_div(hello, string))