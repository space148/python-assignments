def divide_numbers(num1, num2):
    try:
        result = num1 / num2
        print("Result:", result)
    except ZeroDivisionError:
        print("Error: Division by zero is not allowed.")

def main():
    num1 = 10
    num2 = 0
    divide_numbers(num1, num2)

if __name__ == "__main__":
    main()
