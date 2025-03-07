
def divide_numbers(num1, num2):
    try:
        result = num1 / num2
        print(f"Result: {result}")
    except ZeroDivisionError:
        print("Error: Division by zero is not allowed.")
    finally:
        print("Division Completed")

divide_numbers(10, 2)
divide_numbers(10, 0)
