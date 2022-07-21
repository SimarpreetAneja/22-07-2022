a=10
def f():
    print("inside f():",a);
def g():
    a=20
    print("inside g():",a);
def h():
    global a
    a=30
    print("inside h():",a);
print('global:',a)
f()
print("global:",a)
g()
print("global:",a)
h()
print("global:",a)
