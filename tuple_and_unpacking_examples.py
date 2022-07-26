
person = 'Bill', 'Gates', 'Microsoft', '1955-10-28'

shape = 3,
print(shape, type(shape))

print(person[0], person[1])

first_name, last_name, product, dob = person     #  iterable unpacking

people = [
    ('Melinda', 'Gates', 'Gates Foundation', '1964-08-15'),
    ('Steve', 'Jobs', 'Apple', 'NeXT', '1955-02-24'),
    ('Larry', 'Wall', 'Perl', '1954-09-27'),
    ('Paul', 'Allen', 'Microsoft', '1953-01-21'),
    ('Larry', 'Ellison', 'Oracle', '1944-08-17'),
    ('Bill', 'Gates', 'Microsoft', 'Gates Foundation', '1955-10-28'),
    ('Mark', 'Zuckerberg', 'Facebook', '1984-05-14'),
    ('Sergey','Brin', 'Google', '1973-08-21'),
    ('Larry', 'Page', 'Google', '1973-03-26'),
    ('Linus', 'Torvalds', 'Linux', 'Git', '1969-12-28'),
    ('John', 'Strickler', '1962-12-21'),
]

print(f"type(people[0]): {type(people[0])}")
print(f"people[0]: {people[0]}")
print(f"people[0][0]: {people[0][0]}")
print()

# for person in people:
#     first_name, last_name, product, dob = person
#     print(first_name, last_name, dob)
# print('-' * 60)


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

for code, city in airports.items():
    print(code, city)
print()
print(airports.items())
print()

colors = 'red', 'blue', 'green'
for i, color in enumerate(colors):
    print(i, color)
print()

for first_name, last_name, *product, dob in people:
    print(first_name, last_name, product)
print('-' * 60)

values = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']
w, x, y, *z = values
print(w, x, y, z)
w, x, *y, z = values
print(w, x, y, z)
w, *x, y, z = values
print(w, x, y, z)
*w, x, y, z = values
print(w, x, y, z)
