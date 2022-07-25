airports = {
    'EWR': 'Newark',
    'YYZ': 'Toronto',
    'MCI': 'Kansas City',
    'SFO': 'San Francisco',
    'RDU': 'Raleigh-Durham',
    'SJC': 'San Jose',
    'MCO': 'Orlando',
    'YCC': 'Calgary',
    'ABQ': 'Albuquerque',
    'OAK': 'Oakland',
    'SMF': 'Sacramento',
    'YOW': 'Ottawa',
    'IAD': 'Dulles',
}

print(airports['MCO'])
print(airports.get('OAK'))
print(airports.get('FLR'))
print(airports.get('FLR', 'NOT FOUND'))

airports['FLR'] = 'Florence'

print(airports.setdefault('LAS', 'Las Vegas'))
print(f"airports: {airports}")
print()

for code, city in sorted(airports.items()):
    print(code, city)

del airports['MCO']


all_food = ['spam', 'spam', 'spam', 'spam', 'spam', 'spam', 'spam', 'spam', 'spam', 'eggs', 'pudding',
            'spam', 'spam', 'eggs', 'eggs', 'eggs', 'spam', 'spam', 'spam', 'spam', 'spam', 'spam',
            'spam', 'spam', 'spam', 'spam', 'spam', 'spam', 'spam', 'spam', 'toast']

unique_food = set(all_food)
print(f"unique_food: {unique_food}")
print('-' * 60)

colors1 = ['red', 'red', 'blue', 'green', 'purple', 'orange']
colors2 = ['orange', 'red', 'red', 'red', 'red', 'brown', 'black', 'green', 'blue', 'ecru']

c1 = set(colors1)
c2 = set(colors2)

print("common:", c1 & c2)  # intersection
print("not common:", c1 ^ c2)  # xor
print("both:", c1 | c2)  # union
print("only c1:", c1 - c2)
print("only c2:", c2 - c1)

#  { key: value, key: value, key: value, ...}
d = {'foo': 'bar', 'spam': 5, 'ham': 28}











