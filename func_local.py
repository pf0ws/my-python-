#Filename: func_local.py 
def func_local(x):
    print('x is '+ str(x))
    x=2
    print ('change local x to:'+ str(x))
x=5
func_local(x)
print(x)
