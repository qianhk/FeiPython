#!/usr/bin/python
# coding=utf-8

import os
import time

source = ['/PGeneral']
targetDir = '/Bak/backupPython'
target = targetDir + os.sep + time.strftime('%Y%m%d%H%M%S') + '.zip'

if not os.path.exists(targetDir):
    os.mkdir(targetDir)

zipCommand = 'zip -r {0} {1}'.format(target, ' '.join(source))

print ('zip command is: ')
print zipCommand

if os.system(zipCommand) == 0:
    print ('Successful back to', target)
else:
    print ('Backup Failed')


