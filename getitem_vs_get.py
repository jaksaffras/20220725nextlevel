from timeit import Timer

REPEATS = 1000000

setup_code = """
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
"""


code_snippets = [
    """
city = airports['MCO']
    """,
    """
city = airports.get('MCO')
    """,
]

for code_snippet in code_snippets:
    t = Timer(code_snippet, setup_code)
    print("{:60.60s}{}".format(code_snippet, t.timeit(REPEATS)))
    print('-' * 60)
