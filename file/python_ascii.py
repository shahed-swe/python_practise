string = "I love you Abiha"
list1 = []
for i in string:
    print(ord(i), end="\n")
    list1.append(ord(i)+10)
print(list1)
for i in list1:
    print(chr(i), end="")