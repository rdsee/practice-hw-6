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

#2
letters = ['a', 'b', 'c', 'd']
numbers = [1, 2, 6, 4]

dictionary = {}
for i in range(len(letters)):
    dictionary[letters[i]] = numbers[i]
print(dictionary)