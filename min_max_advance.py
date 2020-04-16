def func(item):
    return len(item)

names = ['Shahed Talukder', 'Shahed','Ashik']
print(max(names, key=func))


print(max(names, key=lambda item : len(item)))


students = {
    'shahed':{'score': 90, 'age': 24},
    'ashik':{'score': 80, 'age': 21},
    'azad':{'score': 95, 'age': 23},
}

def func3(item):
    return students[item]['score']

print(max(students, key=func3))

print(max(students, key=lambda item: students[item]['score']))




students2 = [
    {'name': 'shahed','score':90,'age':24},
    {'name': 'ashik','score':80,'age':21},
    {'name': 'azad','score':95,'age':23}
]

def func2(item):
    return item.get('score')

print(max(students2, key=func2))
print(max(students2, key=func2)['name'])
print(type(max(students2, key=func2)))
print(max(students2, key=lambda item: item.get('score')))
print(type(max(students2, key=lambda item: item.get('score'))))
