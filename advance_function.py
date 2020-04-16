def list_sum(l1,l2,l3,l4):
    new_list = []
    for pair in zip(l1,l2,l3,l4):
        new_list.append(sum(pair)/len(pair))
    return new_list

list_sum = lambda l1,l2,l3,l4 : [sum(pair)/len(pair) for pair in zip(l1,l2,l3,l4)]


def list_sum(*args):
    new_list = []
    for pair in zip(*args):
        new_list.append(sum(pair)/len(pair))
    return new_list

list_sum = lambda *args : [sum(pair)/len(pair) for pair in zip(*args)]

def list_sum(l1,l2,l3,l4):
    return [sum(pair)/len(pair) for pair in zip(l1,l2,l3,l3)]

def list_sum(*args):
    return [sum(pair)/len(pair) for pair in zip(*args)]

list1 = [1,2,3,4]
list2 = [5,6,7,8]
list3 = [9,10,11,12]
list4 = [max(pair) for pair in zip(list1,list2)]
print(list_sum(list1,list2,list3,list4))
for pair in list_sum(list1,list2,list3,list4):
    print(pair)

