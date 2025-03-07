class MyException(Exception):
    pass

class MyClass:
    def throw_exception(self):
        raise MyException("This is a custom exception")

def main():
    obj = MyClass()
    obj.throw_exception()

if __name__ == "__main__":
    main()
