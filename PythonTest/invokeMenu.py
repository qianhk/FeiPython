#!/usr/bin/env python
# coding=utf-8

import menu
import sys

reload(sys)
sys.setdefaultencoding('utf-8')

choices = u'item选项1 item选项2 item选项3 item选项4 item选项5 item选项6'.split()

while True:
    userinput = raw_input('试试输入一个选项吧: ')
    if len(userinput) > 0:
        choices.append(userinput)
        if len(choices) >= 8:
            break

print ('in invokeMenu.py', __name__)

menu.showMenuWithTitleAndList('凯尝试选择一项吧:', choices)

print ('in invokeMenu.py', menu.choice_value, menu.choice_index)

if menu.choice_value == 'item选项4':
    print ('guessed 4')
else:
    print ('again')


