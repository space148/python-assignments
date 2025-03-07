def increment(a):
    a+=1
    return a
def decrement(a):
    a-=1
    return a
a=1
print('Increment')
while(a<=10):
    print(a, end = ' ')
    a=increment(a)
print('\ndecrement')
while(a>0):
    print(a, end = ' ')
    a=decrement(a)