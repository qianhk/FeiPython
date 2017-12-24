#!/usr/bin/env python3
# coding=utf-8

import requests
import os

HttpUserAgent = r"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36"


def download(url):
    new_path = os.path.join('..', 'cache')
    print('new_path', new_path)

    if not os.path.isdir(new_path):
        os.makedirs(new_path)

    local_path = os.path.join(new_path, "birthweight.dat")

    if not os.path.exists(local_path):
        response = requests.get(url, headers={'User-Agent': HttpUserAgent})
        if response.status_code != 200:
            print('response {} failed, status_code: {} {}'.format(url, response.status_code, response.reason))
            return

        with open(local_path, 'wb') as local_file:
            local_file.write(response.content)
            local_file.close()

        birth_text = response.text
    else:
        with open(local_path) as local_file:
            birth_text = local_file.read()
    return birth_text


birthdata_url = 'https://github.com/nfmcclure/tensorflow_cookbook/raw/master/01_Introduction/07_Working_with_Data_Sources/birthweight_data/birthweight.dat'

birthText = download(birthdata_url)

# print('birthText', birthText)

birth_data = birthText.split('\n')
print(len(birth_data))
birth_header = birth_data[0].split('\t')
print(birth_header)

birth_data = [[float(x) for x in y.split('\t') if len(x) >= 1] for y in birth_data[1:] if len(y) >= 1]
print(len(birth_data))
print(len(birth_data[0]))
