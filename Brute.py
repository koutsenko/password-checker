#!/usr/bin/env python3

import requests
from threading import Thread

sites = [
    'http://www.google.com',
    'http://habr.com',
    'http://vk.com',
    'http://fb.com',
    'http://www.gmail.com',
]
reqs_per_site = 100

def request(site, count):
    for tryout in range(1, count+1):
        response = requests.get(site)
        print('№', tryout, 'GET', site, response.status_code, len(response.text), 'bytes')


for site in sites:
    Thread(target=request, args=(site, reqs_per_site)).start()
