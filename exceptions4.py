class MyException(Exception):
    pass

def throw_exception(choice):
    if choice == 1:
        raise ValueError("Invalid value")
    elif choice == 2:
        raise TypeError("Invalid type")
    elif choice == 3:
        raise MyException("Custom exception")

def main():
    for choice in range(1, 4):
        try:
            throw_exception(choice)
        except ValueError as ve:
            print(f"Caught ValueError: {ve}")
        except TypeError as te:
            print(f"Caught TypeError: {te}")
        except MyException as me:
            print(f"Caught MyException: {me}")

if __name__ == "__main__":
    main()
