num1 = [1,2,3,4,5,6]
num2 = [2,4,6,8,10]

print(any([i%2 == 0 for i in num2]))
print(all([i % 2 == 0 for i in num1]))


def my_sum(*args):
    check = all([type(i) == int or type(i) == float for i in args])
    if check == True:
        total = 0
        for i in args:
            total += i
        return total
    return "Untyped operand have been passed in this function"

if __name__ == '__main__':
    print(my_sum(1,2,3,5.6,6,7))