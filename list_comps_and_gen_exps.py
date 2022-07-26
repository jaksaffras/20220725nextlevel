
fruits = ["pomegranate", "cherry", "apricot", "apple",
"lemon", "kiwi", "orange", "lime", "watermelon", "guava",
"papaya", "fig", "pear", "banana", "tamarind", "persimmon",
"elderberry", "peach", "blueberry", "lychee", "grape", "date" ]

f0 = []
for f in fruits:
    f0.append(f.upper())
print(f"f0: {f0}\n")

#   [EXPR for VAR in ITERABLE]
f1 = [f.upper() for f in fruits]
print(f"f1: {f1}\n")

f2 = [f.upper() for f in fruits if f.startswith('p')]
print(f"f2: {f2}\n")

f3 = [f for f in fruits if f.startswith('p') if len(f) > 5]
print(f"f3: {f3}\n")

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

codes = [code for code, city in airports.items() if city.startswith('O')]
print(f"codes: {codes}\n")

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

dobs = [p[-1] for p in people]
print(f"dobs: {dobs}\n")

ranks = '2 3 4 5 6 7 8 9 10 J Q K A'.split()
suits = 'Clubs Diamonds Hearts Spades'.split()

cards = [(rank, suit) for suit in suits for rank in ranks]
print(f"cards: {cards}\n")

file_path = 'DATA/breakfast.txt'
with open(file_path) as file_in:
    data = [line.rstrip() for line in file_in]
    print(f"data: {data}\n")

fruit_gen = (f.upper() for f in fruits)
print(f"fruit_gen): {fruit_gen}")

for fruit in fruit_gen:
    print(fruit)
print('-' * 60)

dobs_gen = (p[-1] for p in people)
print(f"dobs_gen: {dobs_gen}")

for dob in dobs_gen:
    print(dob, end=' ')
print("\n")



