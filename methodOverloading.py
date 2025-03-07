class MyClass:
    def my_method(self, *args):
        if len(args) == 1:
            self.one_param(args[0])
        elif len(args) == 2:
            self.two_params(args[0], args[1])

    def one_param(self, param):
        print(f"One parameter: {param}")

    def two_params(self, param1, param2):
        print(f"Two parameters: {param1}, {param2}")

def main():
    obj = MyClass()
    obj.my_method("Hello")
    obj.my_method("Hello", "World")

if __name__ == "__main__":
    main()
