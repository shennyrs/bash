#!/bin/python

all={'name1':"raju",'name2':"praveena",'name3':"george",'name4':"sona"}
girls={'name2':"praveena",'name4':"sona"}
boys={'name1':"raju",'name3':"george"}

for key in list(all.keys()):
    if key in list(girls.keys()):
        print(True)
    else:
        print(False)