peoples_names = ['jim', 'tom', 'andy', 'lily']
nocome_name = peoples_names.pop()

message = f"{nocome_name.title()} is not come."
print(message)

come_name = peoples_names
come_name.append('henry')

message = f"{come_name[0].title()},please come to dinner."
print(message)

message = f"{come_name[1].title()},please come to dinner."
print(message)

message = f"{come_name[2].title()},please come to dinner."
print(message)

message = f"{come_name[3].title()},please come to dinner."
print(message)
