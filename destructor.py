class A:
    def __init__(self):
        print("Hello")
    def display(self):
        print("hi")
    def __del__(self):
        print()
ob=A()
ob.display()
del ob

