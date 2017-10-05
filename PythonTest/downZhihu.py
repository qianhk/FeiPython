#!/usr/bin/env python
# coding=utf-8

import requests
import re
import os

HttpUserAgent = r"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36"


def baidu_zhihu(url):
    #     print('正在下载第'+str(i)+'个页面, 并保存为'+sName)
    count = 0

    # 创建目录保存每个网页上的图片

    page_name = os.path.split(url)[1]
    type_name = os.path.split(os.path.dirname(url))[1]
    new_path = os.path.join('.', type_name, page_name)
    print ('new_path', new_path)

    if not os.path.isdir(new_path):
        os.makedirs(new_path)

    # response = requests.get(url, headers={'User-Agent': HttpUserAgent})
    # if response.status_code != 200:
    #     print ('response {} failed, status_code: {} {}'.format(url, response.status_code, response.reason))
    #     return
    #

    # with open('./zhihu.htm', 'wb') as zhihuPage:
    #     zhihuPage.write(response.content)
    #     zhihuPage.close()

    # page_data = response.text

    with open('./zhihu.htm') as zhihuPage:
        page_data = zhihuPage.read()

    print ('page_data', page_data)

    page_image_pattern = re.compile(r'<img src="(https://.*?\.jpg)"')
    findAllImageUrl = page_image_pattern.findall(page_data)
    for image_url in findAllImageUrl:
        # print (image)
        print ('image_url', image_url)
        image_name_ext = os.path.split(image_url)[1]
        try:
            image_data_response = requests.get(image_url, headers={'User-Agent': HttpUserAgent})
            contentType = image_data_response.headers['Content-Type']
            if image_data_response.ok and contentType.startswith('image/'):
                image_data_content = image_data_response.content
                image_path = os.path.join(new_path, str(count) + '.jpg')
                count += 1
                print(image_path)
                with open(image_path, 'wb') as image_file:
                    image_file.write(image_data_content)
                    image_file.close()
                if count > 10:
                    break
        except BaseException as e:
            print('Download failed', e)


if __name__ == "__main__":
    url = "https://www.zhihu.com/question/35874887"
    baidu_zhihu(url)
