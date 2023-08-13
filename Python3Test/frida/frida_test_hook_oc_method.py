#!/usr/bin/env python3
# coding=utf-8

import sys
import frida

# 进程名
process_name = 'EncodingConvert'
# 导入的js脚本
js_file_name = 'frida_test_hook_oc_method.js'


# https://8biiit.github.io/2019/08/12/Frida/
# Frida在iOS平台进行OC函数hook的常用方法

def on_message(message, data):
    if message['type'] == 'send':
        print('kai1: ' + message['payload'])
    elif message['type'] == 'error':
        print('kai2: ' + message['stack'])


# hook逻辑脚本
def get_js_code():
    js_file = open(js_file_name)
    return js_file.read()


# start here
if __name__ == '__main__':
    session = frida.attach(process_name)
    # 指定JavaScript脚本
    script = session.create_script(get_js_code())
    script.on('message', on_message)
    script.load()
    # 读取返回输入
    sys.stdin.read()
