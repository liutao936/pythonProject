items = ['pen', 'pencil', 'book']
print(items)
items[2] = 'watch'
print(items)
items.append('handbag')
print(items)
items.insert(0,'book')
print(items)
del items[0]
print(items)

item_pop = items.pop(2)
print(item_pop)
print(items)

items.remove('pen')
print(items)

items.append('coat')
items.insert(-1,'dress')
print(items)

print("Here is the original list:")
print(items)

print("\nHere is the sorted list:")
print(sorted(items))

print("\nHere is the original list again:")
print(items)

items.reverse()
print("\nHere is the reverse list:")
print(items)

items.reverse()
print("\nHere is the reverse list again:")
print(items)

items.sort()
print("\nHere is the sort list:")
print(items)

items.sort(reverse=True)
print("\nHere is the reverse sort list:")
print(items)

