#to compare memory location of two objects
#two identity operators used are {is , is not}
x=10
y=10
z=15

if x is y:
    print("x and y have same identity")

if x is z:
    print("x and z have same identity")
else:
    print("x and z have different identity")