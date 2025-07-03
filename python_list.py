# List
items = [2,3,1,3,1,3,3]
item2 = [3,4,2,3,4]

print(items[1:]) # slicing returns a new list
print(items[-3:])

print(items + [134,34,2,3]) 

item2[0] = 43
item2.append(77)

item2.append(2**4) # 2 power 4
print(item2)

newList = [item2, items]
newList2 = item2 + items #array concatination 

print(newList)
print(newList2)

print(newList[0])