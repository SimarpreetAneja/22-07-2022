class A:
    def f1(self):
        print("hello")
class B(A):
    def f2(self):
        print("welcome")
ob=B()
ob.f2()
ob.f1()
