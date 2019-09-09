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


def redirect_to_file(filesize,filepath,redirectfile):
   original = sys.stdout
   sys.stdout = open(redirectfile, 'a')
   print filesize,'\t',filepath
   sys.stdout = original
 

count=1     
mount=sys.argv[1]
unsorted="/tmp/unsorted.txt"
sortedfile="/tmp/sorted.txt"
finalfile="/tmp/output.txt"

#Fetching all the size in the partition and its size
if os.path.exists(unsorted):
   os.remove(unsorted)
if os.path.exists(sortedfile):
   os.remove(sortedfile)
   
for root,dirs,files in os.walk(mount):
   for fn in files:
#     sys.stdout=open(unsorted,'a')
      path=os.path.join(root,fn)
      size=os.stat(path).st_size
#     size=byteconv(os.stat(path).st_size)
#     print int(size),'\t',path
      redirect_to_file(int(size),path,unsorted)

#Sorting the resulted file by size and reversing the file   
input=csv.reader(open(unsorted),delimiter='\t')
sortedlist=sorted(input,key=lambda x:int(x[0]),reverse=True)
with open(sortedfile,"wb") as sf:
   filewrite=csv.writer(sf,delimiter='\t')
   for row in sortedlist:
      filewrite.writerow(row)

output=open(sortedfile,'r')  
for line in output:
   row=line.strip()
   if count <= 20:
      field=row.split('\t')
      conv_size=byteconv(int(field[0]))
      filename=field[1]
      print conv_size,'\t',filename
   count += 1
output.close()

      

#reversing the sorted file to a new file
#with open(sortedfile) as sf:
#   lines=sf.readlines()
#with open(finalfile,'w') as ff:
#   for line in reversed(lines):
#      ff.write(line)

