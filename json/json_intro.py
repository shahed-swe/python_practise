import json

num = [1,2,3,4,5]

filename = 'numbers.json'

with open(filename,'w') as file:
    json.dump(num, file)


with open(filename) as file:
    my_list = json.load(file)

print(my_list[1])