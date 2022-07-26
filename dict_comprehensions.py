import os

file_paths = 'DATA/alice.txt', 'DATA/mystery', 'DATA/mary.txt', 'DATA/presidents.csv', 'DATA/solar.yaml'

file_sizes = {file_path: os.path.getsize(file_path) for file_path in file_paths if not file_path.endswith('yaml')}

print(f"file_sizes: {file_sizes}\n")

#  new_dict = {key:value for var in iterable}

food = ['spam', 'SPAM', 'spam', 'toast', 'eggs', 'Eggs', 'Spam',
        'waffles', 'toast', 'TOAST', 'spam', 'spam', 'spam', 'spam']

unique_food = {f.lower() for f in food if f.lower() != 'spam'}  # set comp
print(f"unique_food: {unique_food}\n")

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

long_names = {code: city for code, city in airports.items() if len(city) > 7}
print(f"long_names: {long_names}\n")
