#!/usr/bin/env python
name={'no1':"shenny",'no2':"neethu"}
age={'shenny':31,'neethu':26}

for i in name:
    me=(name[i])
    myage=str(age[me])
    print("Age of "+ me + " is "+ myage)
    print("Age of "+ (name[i]) + " is " + str(age[(name[i])]))
