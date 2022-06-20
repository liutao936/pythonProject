current_users = ['tom', 'jim', 'henry', 'admin', 'jerry']
new_users = ['lily', 'Jim', 'JOY', 'ADMIN', 'lucy']
for new_user in new_users:
    if new_user.lower() in current_users:
        print(f"{new_user.title()} has already been used.")
    else:
        print(f"{new_user.title()} is available.")
