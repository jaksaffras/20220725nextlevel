#!/usr/bin/env python
import requests

URL = 'http://www.python.org'

response = requests.get(URL)

if response.status_code == requests.codes.OK:  # 200

    for header, value in sorted(response.headers.items()): # <2>
        print("{:20.20s} {}".format(header, value))

    print('-' * 60)

    print(response.text[:500])   # <3>
    print('...')
    print(response.text[-500:])   # <4>
