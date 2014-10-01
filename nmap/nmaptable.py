#!/usr/bin/env python  
#-*- coding: cp1254 -*-
import filecmp
import subprocess
import difflib
d=difflib.Differ()
komut="nmap 255.255.255.255"
i=0
islem = subprocess.Popen(komut, shell = True, stdout = subprocess.PIPE)
cikti = islem.communicate()[0]
dosya= open('/home/melek/nmapfile.txt', 'w+')
dosya.write(cikti)
dosya.close()

