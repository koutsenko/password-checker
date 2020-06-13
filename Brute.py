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

def request(site, tryout):
    try:
        response = requests.get(site)
        print('№', tryout, 'GET', site, response.status_code, len(response.text), 'bytes')
    except:
        print('№', tryout, 'GET', site, 'something get wrong')


def main():
    for site in sites:
        for tryout in range(1, reqs_per_site+1):
            Thread(target=request, args=(site, tryout)).start()

if __name__ == '__main__':
    main()
