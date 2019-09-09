def multiarg(x,y):
    print(x+y)

multiarg(10,15)

#to declare default value of an argument
def arg(a,b=5):
    print(a+b)
    
arg(10)
arg(10)

#changing order
def arg1(x=10,y=3):
    return(x*y)

print(arg1(y=4,x=20))

def multiarg(*moreargs):
    print(moreargs)
    
multiarg(1,2,3,4,5,6,7)