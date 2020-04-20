# w,r+, a --> write mode

# w --> recreate file and write on it
# a --> append text to file or create a file if not exist
# r+ --> over

# with open('file.txt', 'w') as f:
#     f.write('hello\n')
#     f.write('21\n')
    # print(f.read())


# with open('file.txt', 'a') as f:
#     f.write('hello\n')
#     f.write('21\n')
    # print(f.read())


# with open('file.txt', 'r+') as f:
#     f.seek(len(f.read()))
#     f.write('hello\n')
#     f.write('21\n')
#     print(f.read())



# with open('file.txt', 'r') as t:
#     list1 = t.readlines()

# print(list1)


# for i in list1:
#     print(i)



# with open('file.txt', 'r') as rf:
#     with open('file1.txt','w') as wf:
#         wf.write(rf.read())

# with open('file.txt','r') as rf:
#     for i in rf:
#         name,age = i.split(',')
#         print(name,age)


# with open('file.txt','r') as rf:
#     with open('file1.txt','w') as wf:
#         for i in rf:
#             name,salary = i.split(',')
#             wf.write(f"{name}'s' salary is {salary}")
# import pdb

# pdb.set_trace()
def web_url(line):
    if '<a href=' in line:
        pos = line.find('<a href=')
        first_quote = line.find('"', pos)
        second_quote = line.find('"', first_quote+1)
        return f"{line[first_quote+1:second_quote]}\n"
    return ""

with open('index.html','r') as rf:
    with open('output.txt','w') as wf:
        for line in rf.readlines():
            url = web_url(line)
            wf.write(url)