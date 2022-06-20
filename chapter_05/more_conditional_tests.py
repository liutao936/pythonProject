car = 'Subaru'

print("Is car == 'subaru'? I predict True.")
print(car == 'subaru')

print("Is car == 'subaru'? I predict True.")
print(car.lower() == 'subaru')

print("\nIs car == 'audi'? I predict False.")
print(car == 'audi')

age = 20

print("Is age > 18? I predict True.")
print(age > 18)

print("Is age >= 18? I predict True.")
print(age >= 18)

print("Is age <= 18? I predict Flase.")
print(age <= 18)

print("Is age >= 18 and age < 18? I predict True.")
print(age >= 18 and age <18 )

print("Is age >= 18 or age < 18? I predict True.")
print(age >= 18 or age <18 )

cars = ['audi', 'bmw', 'subaru', 'toyota']

car = 'bmw'
if car in cars:
    print(f"{car.title()} in the list.")
car = 'wuling'
if car not in cars:
    print(f"{car.title()} not in the cars list.")

