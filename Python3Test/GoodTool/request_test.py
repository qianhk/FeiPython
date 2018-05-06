#!/usr/bin/env python3
# coding=utf-8

import requests

response = requests.get('https://httpbin.org/ip')
json = response.json()
print('result = %s' % json['origin'])
