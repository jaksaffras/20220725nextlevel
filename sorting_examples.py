
fruits = ["pomegranate", "cherry", "apricot", "Apple",
"lemon", "Kiwi", "ORANGE", "lime", "Watermelon", "guava",
"Papaya", "FIG", "pear", "banana", "Tamarind", "Persimmon",
"elderberry", "peach", "BLUEberry", "lychee", "GRAPE", "date" ]

f0 = sorted(fruits)
print(f"f0: {f0}\n")

def ignore_case(fruit):
    sort_key = fruit.lower()
    print(f"comparing {fruit} as {sort_key}")
    return sort_key

f1 = sorted(fruits, key=ignore_case)
print(f"f1: {f1}\n")

f2 = sorted(fruits, key=str.lower)
print(f"f2: {f2}\n")

#  max() min()

f3 = sorted(fruits, key=len)
print(f"f3: {f3}\n")

def len_and_name(f):
    return len(f), f.lower()

f4 = sorted(fruits, key=len_and_name)
print(f"f4: {f4}\n")

f5 = sorted(fruits, key = lambda f: (len(f), f.lower()))
print(f"f5: {f5}\n")

people = [
    ('Melinda', 'Gates', 'Gates Foundation', '1964-08-15'),
    ('Steve', 'Jobs', 'Apple', '1955-02-24'),
    ('Larry', 'Wall', 'Perl', '1954-09-27'),
    ('Paul', 'Allen', 'Microsoft', '1953-01-21'),
    ('Larry', 'Ellison', 'Oracle', '1944-08-17'),
    ('Bill', 'Gates', 'Microsoft', '1955-10-28'),
    ('Mark', 'Zuckerberg', 'Facebook', '1984-05-14'),
    ('Sergey','Brin', 'Google', '1973-08-21'),
    ('Larry', 'Page', 'Google', '1973-03-26'),
    ('Linus', 'Torvalds', 'Linux', '1969-12-28'),
]

for person in sorted(people, key=lambda p: p[-1]):
    print(person)
print('-' * 60)

def last_first(p):
    return p[1], p[0]

for person in sorted(people, key=last_first):
    print(person)
print('-' * 60)

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

for code, city in sorted(airports.items()):
    print(code, city)
print('-' * 60)

for code, city in sorted(airports.items(), key=lambda e: (e[1], e[0])):
    print(code, city)
print('-' * 60)
