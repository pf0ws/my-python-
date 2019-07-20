#Fliename:func_global.py
def func():
    global x
    print('x is',x)
    x=2
    print ('chang local x to',x)
x=30
func()
print('value x is',x)