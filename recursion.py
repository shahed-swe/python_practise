# here we will discuss about recursion
# factorial problem
def factorial(n):
    '''this function return the factorial number'''
    if n == 1:
        return 1
    return n * factorial(n-1)
# out put will be the factorial of the number is given


# reverse order problem
def print_rev(i,n, a):
    '''this function basically returns your given array in reverse order and print it'''
    if(i < n):
        print_rev(i+1, n, a)
        print(f"{a[i]}")

# Input:
# 5
# 69 87 45 21 47
# Output:
# 47 21 45 87 69

def printing_method(i, j, a):
    '''this function basically print the given array in box sequence'''
    if i <= j:
        print(f"{a[i]} {a[j]}")
        printing_method(i+1, j-1, a)
# Input:
# 5
# 1 5 7 8 9
# Output:
# 1 9
# 5 8
# 7 7


# def remove_odd_int(i,j,n,a):
#     if(i == n):
#         n = j
#         return
#     if a[i] % 2 == 0:
#         j += 1
#         a[j] = a[i]
#     remove_odd_int(i+1, j,n,a)

if __name__ == '__main__':
    number = factorial(4)
    print(number)
    # for next problem
    list1 = [3,5,6,12,17]
    print_rev(0, len(list1), list1)
    # for next problem
    printing_method(0, len(list1)-1, list1)
    # for next problem
    # remove_odd_int(0,0,len(list1), list1)
    # for i in list1:
    #     print(i)
