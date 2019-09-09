#!/usr/bin/env python2

__author__ = '{author}'
__copyright__ = 'Copyright {year}, {project_name}'
__credits__ = ['{credit_list}']
__license__ = '{license}'
__version__ = '{mayor}.{minor}.{rel}'
__maintainer__ = '{maintainer}'
__email__ = '{contact_email}'
__status__ = '{dev_status}'

# Generic/Built-in
import os
import sys
import csv
import time
import socket
import subprocess

# script usage
def usage():
   script=sys.argv[0]
   print "Usage:\t",script, " <mount>\n"
   sys.exit()

# checking for arguments
def argcheck():
   if len(sys.argv)!=2:
      usage()

#checking if input directory exist & if it's a mount or not
def isdir(path):
   if not os.path.isdir(path):
      print "No such Mount point: ",path,"\n"
      sys.exit()   
   if not os.path.ismount(path):
      dirname=path
      path=os.path.abspath(path)
      while not os.path.ismount(path):
         path=os.path.dirname(path)
      print dirname," is a directory in mountpoint",path,"\n"

#creating boundary around output
def boundary(mystring=0):
   line="-"*70
   if mystring==0:
      print line,"\n"
   else:
      haystack=len(mystring)
      needle=(70 - haystack)/2
      if haystack % 2 == 0:
         needle=needle-1
      print "-"*needle,mystring,"-"*needle     

# converting bytes to kb,mb,gb and tb
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

#redirecting stdout to a file without printing
def redirect_to_file(filesize,filepath,redirectfile):
   original = sys.stdout
   sys.stdout = open(redirectfile, 'a')
   print filesize,'\t',filepath
   sys.stdout = original
 
argcheck()
count=1   
mount=sys.argv[1]
now=time.strftime("%c")
unsorted="/tmp/unsorted.txt"
sortedfile="/tmp/sorted.txt"
finalfile="/tmp/output.txt"

# fetching os details and mount size
boundary()
print socket.getfqdn(),"Current date: %s" % now
boundary()
isdir(mount)
boundary("Current Disk Usage")
subprocess.call(["df","-hP",mount])
boundary()

#Removing input-unsorted_list and output-sorted_list if exist
if os.path.exists(unsorted):
   os.remove(unsorted)
if os.path.exists(sortedfile):
   os.remove(sortedfile)
   
#Recursevely fetching files in the input directory   
for root,dirs,files in os.walk(mount):
   for fn in files:
      path=os.path.join(root,fn)
      if not os.path.islink(path):
         size=os.stat(path).st_size
         redirect_to_file(int(size),path,unsorted)

#Sorting the resulted file by size and reversing the file   
input=csv.reader(open(unsorted),delimiter='\t')
sortedlist=sorted(input,key=lambda x:int(x[0]),reverse=True)
with open(sortedfile,"wb") as sf:
   filewrite=csv.writer(sf,delimiter='\t')
   for row in sortedlist:
      filewrite.writerow(row)

#printing top 20 sized files
boundary("Largest 20 files")
output=open(sortedfile,'r')
for line in output:
   row=line.strip()
   if count <= 20:
      field=row.split('\t')
      conv_size=byteconv(int(field[0]))
      filename=field[1]
      print("%-20s %4s" % (conv_size, filename))
   count += 1

output.close()
boundary()
