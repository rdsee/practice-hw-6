#1
countries = {
    "France":["Marcel", "Paris", "Brno"],
    "USA":["Los Angeles", "Miami", "Washington"],
    "Poland":["Warsaw", "Krakow", "Gdansk"]
}

countries2 = {}
for key, value in countries.items():
    print(f"{key} -> {value}")
    for city in value:
        countries2[city] = key
print(countries2)

