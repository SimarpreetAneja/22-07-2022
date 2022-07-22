class A:
    
    def f1(self):
        print("f1")
    def __init__(self):
        print("contructor")
class B:
   
    def __init__(self):
        
        print("b class")
    def f2(self):
        print(self)
ob=B()
ob.f2(30)
 
