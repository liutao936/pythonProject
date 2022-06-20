my_pizzas = ['peperoni', 'ham', 'fruit']
friend_pizzas = my_pizzas[:]

my_pizzas.append('nut')
friend_pizzas.append('banana')

print(f"My favorite pizzas are:")
for my_pizza in my_pizzas:
    print(my_pizza)

print(f"My friend's favorite pizzas are:")
for friend_pizza in friend_pizzas:
    print(friend_pizza)


