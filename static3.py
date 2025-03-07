class myClass:
    a=10
    def __init__(self):
        pass
    def change(self,n):
        myClass.a=n
print(myClass.a)
instance = myClass()
print(instance.a)
instance.change(11)
print(instance.a)