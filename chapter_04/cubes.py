numbers = list(range(1, 11))
for number in numbers:
    cube = number ** 3
    print(cube)

cubes = []
for value in range(1, 11):
    cube = value ** 3
    cubes.append(cube)
print(cubes)