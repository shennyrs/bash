def myfun(x,y,z):
    if x>y and x>z:
        print(x,"is the larger than",y,"and",z)
    elif y>x and y>z:
        print(y,"is the larger than",x,"and",z)
    elif z>x and z>y:
        print(z,"is the larger than",x,"and",y)
    elif x==y and x==z:
        print(x,y,z,"are equal")
    else:
        print("no defined condition")
        
myfun(10,5,2)
myfun(1,2,3)
myfun(5,10,7)
myfun(1,1,1)
myfun(1,2,1)