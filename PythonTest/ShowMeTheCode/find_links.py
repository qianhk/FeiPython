#!/usr/bin/env python
# coding=utf-8

import requests
import pyquery

HttpUserAgent = r"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36"

def find_links(url):
    list = []
    html = get_html(url)
    doc = pyquery.PyQuery(html)
    a_tags = doc.find('a')
    for a in a_tags.items():
        hrefAttr = a.attr('href')
        if isinstance(hrefAttr, str) and len(hrefAttr) > 0:
            if hrefAttr.startswith('http'):
                list.append(hrefAttr)
            elif hrefAttr.startswith('/'):
                list.append('' + hrefAttr)

    # for item in list:
    #     print item

    imgList = []
    imgTags = doc.find('img').items()
    for imgTag in imgTags:
        imgSrc = imgTag.attr['src']
        if isinstance(imgSrc, str) and len(imgSrc) > 0 and imgSrc.startswith('http'):
            imgList.append(imgSrc)
    for imgUrl in imgList:
        print imgUrl

def get_html(url):
    response = requests.get(url, headers={'User-Agent': HttpUserAgent})
    return response.text

if __name__ == '__main__':
    url = 'http://tieba.baidu.com/p/2166231880'
    find_links(url)

