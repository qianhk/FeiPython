#!/usr/bin/env python
# coding=utf-8

import os
import platform
import logging
import sys

#mac is :  Darwin-16.7.0-x86_64-i386-64bit
print (platform.platform())

loggingFile = sys.argv[0]
loggingFile = os.path.join(os.path.dirname(loggingFile), "./cache/test.log")
print ('Logging to', loggingFile)

logging.basicConfig(level=logging.INFO, format='%(asctime)s : %(levelname)s : %(message)s', filename=loggingFile, filemode='w',)

logging.debug("Start of the program")
logging.info("Doing something")
logging.warning("Dying now")

