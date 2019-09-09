#creating empty list
mylist=[]

#addition of element
mylist.append(1)
mylist.append(2)
mylist.append(3)
for i in range(0,3):
    print("value" ,i, "is",mylist[i])
    
#adding element to the list
for j in range(4,10):
    mylist.append(j)
print(mylist)

mylist.append((11,12))
print(mylist)

#adding list to a list
list1=["hello","world"]
mylist.append(list1)
print(mylist)

#postion and value
for i in range(0,11):
    print("value at position",i,"is",mylist[i])

print(" ")
mylist.insert(5,100)
c=0
for i in mylist:
    print("value at postion",c,"is",mylist[c])
    c=c+1
    
#adding multiple element to the list at the end
print(" ")
mylist.extend(["shenny"])
c=0
for i in mylist:
    print("value at postion",c,"is",mylist[c])
    c=c+1


    