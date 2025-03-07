class MyClass:
    a = 10

    def __init__(self):
        pass

    def static_variable(self):
        return MyClass.a

my_instance = MyClass()
print(my_instance.static_variable())
