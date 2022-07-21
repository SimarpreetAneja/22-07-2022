class A:
    def __init__(self):
        print("hell")
    def __str__(self):
       return "hello"
    def __del__(self):
        print("hello")
ob=A()
print(ob)
