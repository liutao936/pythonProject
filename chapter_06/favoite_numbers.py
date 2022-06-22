favorite_numbers = {'mandy': [42, 17], 'micah': [42, 39, 56], 'gus': [7, 12], }
for name, numbers in favorite_numbers.items():
    print(f"\n{name.title()} like the following numbers:")
    for number in numbers:
        print(f"\t{number}")
        
