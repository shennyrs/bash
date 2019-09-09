a="hello"
print("global=>"+a)

def myprint():
    a="world"
    print("local=>"+a)

myprint()
print(a)