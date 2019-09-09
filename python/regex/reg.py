import re

mystring="this is my test string"
mynum="hello 123456 world"
out1=re.findall(r"\w+$",mystring)


print(out1)

print(re.findall(r"\d{1,4}",mynum))