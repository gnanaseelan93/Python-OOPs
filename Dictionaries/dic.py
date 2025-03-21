map = {1: 'one', 2: 'two', 3: 'three'}
print(map)
print(map[1])

print(type(map))

#add
map[4] ='four'
print(map)

#update
map[1] ='ONE'
print(map)

#delete
del map[1]
print(map)

#GET
print(map.get(2))

#LENGTH
print(len(map))

#keys
print(map.keys())

#values
print(map.values())

#items
print(map.items())

#pop
map.pop(2)
print(map)

#popitem
map.popitem()
print(map)

#copy
map2 = map.copy()
print(map2)

#update
map2.update({1:'one'})
print(map2)


#clear
map.clear()
print(map)