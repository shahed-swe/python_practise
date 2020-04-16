names = ['shahed','ashik','rajib','atik']
names2 = ('shahed','ashik','rajib','atik')
names3 = {'shahed','ashik','rajib','atik'}
# names.sort()



new_sort = sorted(names)
new_sort2 = sorted(names2)
new_sort3 = sorted(names3)
print(new_sort)
print(new_sort2)
print(new_sort3)

guiters = [
    {'models':'signature','price':1200},
    {'models':'yamaha','price':900},
    {'models':'lalabu','price':1300},
    {'models':'ukuele','price':570},
]

get = sorted(guiters, key=lambda d: d.get('price'))
get2 = sorted(guiters, key=lambda d: d.get('price'),reverse=True)
print(get)
print(get2)