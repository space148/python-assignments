class MyClass:
    def my_method(self, *args):
        if len(args) == 1 and isinstance(args[0], int):
            self.one_int_param(args[0])
        elif len(args) == 2 and isinstance(args[0], str) and isinstance(args[1], float):
            self.str_float_params(args[0], args[1])

    def one_int_param(self, param):
        print(f"One integer parameter: {param}")

    def str_float_params(self, param1, param2):
        print(f"String and float parameters: {param1}, {param2}")

def main():
    obj = MyClass()
    obj.my_method(123)
    obj.my_method("Hello", 45.67)

if __name__ == "__main__":
    main()
