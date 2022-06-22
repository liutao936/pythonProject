favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}

friends = ['phil', 'sarah', 'jim']

for friend in friends:
    if friend in favorite_languages.keys():
        print(f"{friend.title()},thanking you for responding.")
    else:
        print(f"{friend.title()},please to take the poll.")
