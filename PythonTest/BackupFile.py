#!/usr/bin/env python
# coding=utf-8

import sys
import os
import time
import zipfile

print ('Python info: {}'.format(sys.version))

# def mkdir_p(path):
#     try:
#         os.makedirs(path)
#     except OSError as exc: # Python >2.5 (except OSError, exc: for Python <2.5)
#         if exc.errno == errno.EEXIST and os.path.isdir(path):
#             pass
#         else: raise



source = ['/PGeneral']
targetDir = '/Bak/backupPython'
today = targetDir + os.sep + time.strftime('%Y%m%d')

try:
    comment = raw_input('Enter a comment -->')
except NameError as error:
    comment = input('Enter a comment -->')

now = time.strftime('%H%M%S')
if len(comment) == 0:
    target = today + os.sep + now + '.zip'
else:
    target = today + os.sep + now + '_' + comment.replace(' ', '_') + '.zip'

if not os.path.exists(today):
    os.makedirs(today)



# zipCommand = 'zip -r {0} {1}'.format(target, ' '.join(source))
#
# print ('zip command is: ')
# print (zipCommand)
#
# if os.system(zipCommand) == 0:
#     print ('Successful back to', target)
# else:
#     print ('Backup Failed')

def get_items_list_in_dir(src, lst):
    listdir = os.listdir(src)
    for itemInDir in listdir:
        if itemInDir == '.DS_Store':
            continue
        path = os.path.join(src, itemInDir)
        lst.append(path)
        if os.path.isdir(path):
            get_items_list_in_dir(path, lst)


singleSource = source[0]
itemList = [singleSource]
get_items_list_in_dir(singleSource, itemList)

os_walk = os.walk(singleSource)
for dirpath, dirnames, filenames in os_walk:
    print (dirpath, dirnames, filenames)

with zipfile.ZipFile(target, 'w', zipfile.ZIP_DEFLATED) as myZip:
    for item in itemList:
        myZip.write(item)
    myZip.close()






