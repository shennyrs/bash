#!/usr/bin/env python2
import os
import sys
import csv

def byteconv(size):
   kb=float(1024)
   mb=float(kb*1024)
   gb=float(mb*1024)
   tb=float(gb*1024)
   if 0 <= size <  1024:
      return str(size)+"B"
   elif kb <= size < mb:
      inkb=float(size / kb)
      return str("{0:0.1f}".format(inkb))+"KB"
   elif mb <= size < gb:
      inmb=float(size / mb)
      return str("{0:0.1f}".format(inmb))+"MB"
   elif gb <=size < tb:
      ingb=float(size / gb)
      return str("{0:0.1f}".format(ingb))+"GB"
   else:
      intb=float(size /tb)
      return str("{0:0.1f}".format(intb))+"TB"
   
   
size=sys.argv[1]
output=byteconv(int(size))
print output