#!/usr/bin/env python3
# coding=utf-8


import requests
import time
import os
# import uuid
import re
import sys

vote_url = 'https://opensea.io/collection/art-of-mob'

USER_AGENT = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/69.0.3497.92 Safari/537.36'


def do_get_html():
    headers = {'User-Agent': USER_AGENT, 'Referer': vote_url}

    try:
        response = requests.post(vote_url, headers=headers, verify=False)
        return response.text
    except (TimeoutError, ConnectionError):
        return '<title>404'
    except:
        return 'unknownException' + str(sys.exc_info())


def append_log_to_file(_filename, _msg):
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    fo = open(_filename, "a")
    # fo.seek(0, 2)
    fo.write(_msg + '\n')
    fo.close()


if __name__ == "__main__":
    # print('python file dir:' + pyfiledir)
    html = do_get_html()
    print(f'lookKai artOfMob url={vote_url} context={html}')
