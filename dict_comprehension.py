# Long version of code
dict = {}
for i in range(1, 5):
    dict[i] = i * 2
print(dict)    

# Short version of code with dict comprehension
dict_v2 = { i: i * 2 for i in range(1, 5)}
print(dict_v2)


# dict comprehension with List 1
import random
countries = ['col', 'mex', 'us', 'pe']
population = {}
for country in countries:
    population[country] = random.randint(1000, 10000)
print(population)

population_v2 = {country: random.randint(1000, 10000) for country in countries}
print(population_v2)


# dict comprehension with List 2
names = ['nico', 'zule', 'santi']
ages = [12, 44, 53]
print(list(zip(names, ages)))

new_dict = {name: age for (name, age) in zip(names, ages)}
print(new_dict)


# dict comprehension with: for
brands = ['apple', 'tesla', 'meta']

market_share = { brand: random.randint(0, 1000) for brand in brands}
print(market_share)

top_ones = {brand: market for (brand, market) in market_share.items() if market > 500}
print(top_ones)


# dict comprehension with: if
text = 'Hey I am a programmer'
unique = { c: c.upper() for c in text if c in 'aeiou'}
print(unique)