sandwich_orders = ['sandwich1', 'sandwich2', 'sandwich3']
finished_sandwiches = []
while sandwich_orders:
    sandwich = sandwich_orders.pop()
    print(f"I made your {sandwich} sandwich.")
    finished_sandwiches.append(sandwich)
for finished_sandwiche in finished_sandwiches:
    print(f"{finished_sandwiche} sandwich that was made.")
