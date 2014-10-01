#!/usr/bin/env python  
#-*- coding: cp1254 -*-
import filecmp
import subprocess
import difflib
d=difflib.Differ()
komut="arp -a"
i=0
islem = subprocess.Popen(komut, shell = True, stdout = subprocess.PIPE)
cikti = islem.communicate()[0]
cikti = cikti.strip('dsldevice.Home')
cikti = cikti.strip('[ether] on wlan0')
dosya= open('/home/melek/mainfile.txt', 'w+')
dosya.write(cikti)
dosya.close()

