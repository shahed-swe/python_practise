# read file
# open function
# read method
# seek method
# tell method
# readline method
# readlines method
# close method
f = open('file.txt')
# print(f.readline())
# print(f"curson position {f.tell()}") #tto know the position of curson
# print(f.readline())
# f.seek(23) #seek method move the cursor

# print(f.read())
print(f.readlines())
print(f.name)
print(f.closed)


f.close()
print(f.closed)
f = open(r'C:\Users\Shahed\Desktop\python_practise\advance_function.py')
# print(f.read())

# for line in f:
#     print(line, end ='>>> ')

# print(f.readlines())
for i in f.readlines()[:5]:
    print(i, end="")

f.close()