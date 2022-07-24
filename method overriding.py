class Parent:
    def display(self):
        print("inside parent")
class Child(Parent):
    def display(self):
        print("inside child")
ob=Child()
ob.display()
ob=Parent()
ob.display()
