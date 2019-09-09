#!/usr/bin/python2

import os
import sys
import subprocess
import socket
import time

def usage():
   script=sys.argv[0]
   print "Usage:\t",script, " <mount>\n"
   sys.exit()

def argcheck():
   if len(sys.argv)!=2:
      usage()

def isdir(path):
    if not os.path.ismount(path):
        print path," is a directory in mountpoint\n"
        sys.exit()


argcheck()
mount=sys.argv[1]
now=time.strftime("%c")
diskusage=open("dfres","w")
subprocess.Popen(["df","-hP"],stdout=diskusage)

print "*" * 60
print "Hostname: ",socket.gethostname(),"Current date: %s" % now
print "*" * 60,"\n"

isdir(mount)

subprocess.call(["df","-hP",mount])
print " "
diskusage.close()
