def city_country(city, country):
    """返回一个类似于'Santiago, Chile'的字符串。"""
    message = f"{city.title()}, {country.title()}"
    return message


city = city_country('santiago', 'chile')
print(city)

city = city_country('ushuaia', 'argentina')
print(city)

city = city_country('longyearbyen', 'svalbard')
print(city)
