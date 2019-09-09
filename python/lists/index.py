list1=["hello","world"]
print(list1[0])

list1=[["shenny","rs"],["renny","rs"]]
print(list1)
print(list1[0][0])

#printing last element
list1=[100,101,102,103,104,105]
print(list1[-1])

#print 2nd last element
print(list1[-2])

#removing element
c=0
for i in list1:
   print("value at position",c,"is",list1[c])
   c=c+1
list1.remove(4)

c=0
for i in list1:
   print("value at position",c,"is",list1[c])
   c=c+1