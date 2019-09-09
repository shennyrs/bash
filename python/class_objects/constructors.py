#constructor is a class function that instantiates an object to predefined values
#defined with a double underscore() it is __init__() method

class user():
    name=" "
    def __init__(self, name):
        self.name=name
    def sayhello(self):
        print("hello "+self.name)
        
user1=user("alex")
user1.sayhello()