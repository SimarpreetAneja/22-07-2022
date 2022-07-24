class A:
   def __init__(self,txt):
        print("hi")
class B(A):
    def __init__(self,txt):
        super().__init__(txt)
        print("hello")
obj= B("hi")
