class MyClass:
    def my_method(self, param1, param2):
        if isinstance(param1, int) and isinstance(param2, int):
            self.int_params(param1, param2)
        elif isinstance(param1, str) and isinstance(param2, str):
            self.str_params(param1, param2)

    def int_params(self, param1, param2):
        print(f"Integer parameters: {param1}, {param2}")
        print(f"Sum: {param1 + param2}")

    def str_params(self, param1, param2):
        print(f"String parameters: {param1}, {param2}")
        print(f"Concatenated: {param1 + param2}")

def main():
    obj = MyClass()
    obj.my_method(123, 456)
    obj.my_method("Hello", "World")

if __name__ == "__main__":
    main()
