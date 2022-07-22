class A:
    a=10
    def f1(self):
        print("f1")
    def __init__(self):
        print("contructor")
class B:
    b=20
    def __init__(self):
        
        print("b class")
    def f2(self,b):
        print(self.b)
ob=B()
ob.f2(30)
 
