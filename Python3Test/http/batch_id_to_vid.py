#!/usr/bin/env python3
# coding=utf-8

import requests
import os
import json
import click
import csv


# from pathlib import Path


def get_id_list_from_local_file(ori_json_file):
    # path = Path(ori_json_file)
    ori_json_file = os.path.normpath(ori_json_file)
    number_id_list = []
    with open(ori_json_file, 'r') as f:
        json_data_list = json.load(f)
        # print(json_data_list)
        for item_dic in json_data_list:
            number_id_list.append(item_dic['iid'])
    return number_id_list


def get_vid_from_net(base_url, numberId):
    url = f'{base_url}{numberId}'
    print('get data from url: ' + url)
    response = requests.get(url)
    # print(response.text)
    json_list = response.json()['data']
    length = len(json_list)
    if length != 1:
        raise NameError(f'子元素数量不对:{length}')
    item_json = json_list[0];
    return [item_json['encoded_id'], item_json['snippet']['title']]


@click.command()
@click.option("--ori", help="local number id json file")
@click.option("--base-url", help="base url")
def convert_id_to_vid(ori, base_url):
    print(f'ori={ori} base_url={base_url}')
    id_list = get_id_list_from_local_file(ori)
    print(f'id_list length = {len(id_list)}')

    # with open('../cache/vid.csv', 'w') as csv_file:
    #     fieldnames = ['vid', 'title']
    #     writer = csv.DictWriter(csv_file, fieldnames=fieldnames)
    #     vid_json = get_vid_from_net(base_url, id_list[0])
    #     # csv_file.write(",".join(vid_json) + "\n")
    #     writer.writeheader()
    #     writer.writerow({fieldnames[0]: vid_json[0], fieldnames[1]: vid_json[1]})
    #     # print(f'vid_json={vid_json}')

    with open('../cache/vid.csv', 'w') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(['vid', 'title'])
        # vid_title = get_vid_from_net(base_url, id_list[0])
        # writer.writerow(vid_title)
        # writer.writerow([s.encode("utf-8") for s in vid_title])
        for number_id in id_list:
            vid_title = get_vid_from_net(base_url, number_id)
            writer.writerow(vid_title)

    print('Done.')


if __name__ == '__main__':
    convert_id_to_vid()
