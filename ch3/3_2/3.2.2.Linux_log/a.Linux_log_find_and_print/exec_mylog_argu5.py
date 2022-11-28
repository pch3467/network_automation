#!/bin/env python
#-*- coding: utf-8 -*-

import mylog_5
import os

logfile = "/var/log/boot.log.1"
file_length = os.path.getsize(logfile)

mylog_5.printlog(logfile, "failed", int(file_length/2), 3, 5)
