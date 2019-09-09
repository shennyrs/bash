class myclass1():
    def fun1(self):
        print("hello world")
        
class myclass2(myclass1):
    def fun2(self):
        print("your world")
        
def fun3():
    c1=myclass1()
    c2=myclass2()
    print("invoking myclass1")
    c1.fun1()
    print("*****************")
    print("invoking myclass2")
    c2.fun1()
    c2.fun2()
    print("*****************")
    
fun3()