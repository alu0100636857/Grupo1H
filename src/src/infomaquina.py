#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Autor: Vanesa Abad Armas
# Módulo infomativo sobre la máquina computacional
import os
import platform

def CPUinfo():
 infofile = "/proc/cpuinfo"
 cpuinfo = {}
 if os.path.isfile(infofile):
   f = open(infofile, 'r')
   for line in f:
     try:
	name, value = [w.strip() for w in line.split(':')]
     except:
	continue
     if name == 'model name':
       cpuinfo['CPU type'] = value
     elif name == 'cache size':
       cpuinfo['cache size'] = value
     elif name == 'cpu MHz':
       cpuinfo['CPU speed'] = value + ' Hz'
     elif name == 'vendor_id':
       cpuinfo['vendor ID'] = value
   f.close()
 return cpuinfo

if __name__ == "__main__":
  fichero=open('informacion.txt','w')
  fichero.write("{0}\n{1}\n{2}\n{3}".format(CPUinfo(),platform.uname(),platform.platform(),platform.python_build()))
  fichero.close()
