cities = {
    'santiago': {
        'country': 'chile',
        'population': 6_310_000,
        'nearby mountains': 'andes',
    },
    'talkeetna': {
        'country': 'united states',
        'population': 876,
        'nearby mountains': 'alaska range',
    },
    'kathmandu': {
        'country': 'nepal',
        'population': 975_453,
        'nearby mountains': 'himilaya',
    }
}
for cities_name, cities_info in cities.items():
    cities_country = cities_info['country'].title()
    cities_population = cities_info['population']
    cities_mountains = cities_info['nearby mountains'].title()

    print(f"\n{cities_name.title()} is in {cities_country}.")
    print(f"\tIt has a population of about {cities_population}.")
    print(f"\tThe {cities_mountains} mounats are nearby.")
