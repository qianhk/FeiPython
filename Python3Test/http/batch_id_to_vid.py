#!/usr/bin/env python3
# coding=utf-8

import requests
import os
import json
import click
import csv
import sys


# from pathlib import Path


def get_id_list_from_local_file(ori_json_file):
    # path = Path(ori_json_file)
    ori_json_file = os.path.normpath(ori_json_file)
    try:
        number_id_list = []
        with open(ori_json_file, 'r') as f:
            json_data_list = json.load(f)
            # print(json_data_list)
            for item_dic in json_data_list:
                number_id_list.append(item_dic['iid'])
        return number_id_list
    except:
        info = sys.exc_info()[0]
        click.echo(f'open file ({ori_json_file}) Unexpected error: ', nl=False)  # This will prevent the secho statement from starting a new line
        click.secho(f'{info}', fg='red')
        # click.secho(f"open file ({ori_json_file}) Unexpected error: {sys.exc_info()[0]}", fg='red')
        return None


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
@click.option("--base-url", "-u", "base_url2", help="base url")
@click.option('--mode', type=click.Choice(['read-only', 'read-write']))
@click.option('--env-value', envvar='DEVELOPER_DIR', type=click.STRING)
@click.argument("local-json", type=click.Path(exists=False))
@click.argument("local-json2", type=click.Path(exists=False))
@click.argument('foo', nargs=-1, required=False)
# @click.option('-n', default=1)
# @click.option('--message', '-m', multiple=True)
# @click.option('-v', '--verbose', count=True)
# @click.option('--shout', is_flag=True)
# @click.option('--shout/--no-shout', default=False)
# @click.option('/debug;/no-debug') #在 Windows 中，一个选项可以以 / 开头，这样就会真假选项的分隔符冲突了，这个时候可以使用 ; 进行分隔：
# @click.option('--upper', 'transformation', flag_value='upper', default=True)
# @click.option('--lower', 'transformation', flag_value='lower')
# @click.option('--hash-type', type=click.Choice(['MD5', 'SHA1'], case_sensitive=False))
# @click.option('--name', prompt=True)
# @click.password_option()
# @click.option('--count', type=click.IntRange(0, None, clamp=True))
# @click.option('--digit', type=click.IntRange(0, 10))
# @click.option('--yes', is_flag=True, callback=abort_if_false, expose_value=False, prompt='Are you sure you want to drop the db?')
# @click.confirmation_option(prompt='Are you sure you want to drop the db?')
def convert_id_to_vid(local_json, base_url2, local_json2, mode, env_value, foo):
    base_url = base_url2
    print(f'local_json={local_json} base_url={base_url}')
    print(f'local_json2={local_json2}')
    click.echo(f'mode={mode}')
    click.echo(f'env_value={env_value}')
    click.echo(f'foo={foo}')
    click.secho(local_json2, fg='green')
    click.echo(click.format_filename(local_json2), color='blue')
    id_list = get_id_list_from_local_file(local_json)
    if id_list is None:
        return

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
        vid_title = get_vid_from_net(base_url, id_list[0])
        writer.writerow(vid_title)
        print(vid_title)
        # writer.writerow([s.encode("utf-8") for s in vid_title])
        # for number_id in id_list:
        #     vid_title = get_vid_from_net(base_url, number_id)
        #     writer.writerow(vid_title)

    print('Done.')


if __name__ == '__main__':
    convert_id_to_vid()
