age = 12
if age < 4:
    print("You admission is $0.")
elif age < 18:
    print("You admission is $25.")
else:
    print("You admission is $40.")

age = 72
if age < 4:
    price = 0
elif age < 18:
    price = 25
elif age < 65:
    price = 40
else:
    price = 20

print(f"You admission is ${price}.")
