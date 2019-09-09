class myclass():
    def myfun1(self):
        print("hello world")
    def myfun2(self,mystring):
        print("your world" + mystring)
        
def main():
    c=myclass()
    c.myfun1()
    c.myfun2(" is my world")
    
main()