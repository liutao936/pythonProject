places = ['beijing', 'shanghai', 'hangzhou', 'xian' ,'chongqi']

print("Here is the original list:")
print(places)

print("\nHere is the sorted list:")
print(sorted(places))

print("\nHere is the original list again:")
print(places)

places.reverse()
print("\nHere is the reverse list:")
print(places)

places.reverse()
print("\nHere is the reverse list again:")
print(places)

places.sort()
print("\nHere is the sort list:")
print(places)

places.sort(reverse=True)
print("\nHere is the reverse sort list:")
print(places)
