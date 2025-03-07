a=10                #global variable
def myFunction(b):
    a=9             #local variable
    print('local variable: a = ',a)
    print('sum: ',a+b)
print('global variable: a = ',a)
myFunction(a)