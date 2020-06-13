#!/usr/bin/env python3

import requests

sites = [
    'http://www.google.com',
    'http://habr.com',
    'http://vk.com',
    'http://fb.com',
    'http://www.gmail.com',
]

for tryout in range(100):
    for site in sites:
        response = requests.get(site)
        print('№', tryout, 'GET', site, response.status_code, len(response.text), 'bytes')

