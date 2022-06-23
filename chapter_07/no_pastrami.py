sandwich_orders = ['pastrami', 'sandwich1', 'pastrami', 'sandwich2', 'pastrami', 'sandwich3']
finished_sandwiches = []
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')
while sandwich_orders:
    sandwich = sandwich_orders.pop()
    print(f"I made your {sandwich} sandwich.")
    finished_sandwiches.append(sandwich)
for finished_sandwiche in finished_sandwiches:
    print(f"{finished_sandwiche} sandwich that was made.")
