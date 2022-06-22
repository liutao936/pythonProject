rivers = {'nile': 'egypt', 'huanghe': 'china', 'changjiang': 'china'}
for k, v in rivers.items():
    print(f"The {k.title()} runs through {v}.")

print("Rivers name is:")
for k in rivers.keys():
    print(f"\t{k}")

print("Country name is：")
for v in rivers.values():
    print(f"\t{v}")
    
