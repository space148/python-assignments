def divide_numbers(num1, num2):
    result = num1 / num2
    print(f"Result: {result}")

try:
    divide_numbers(10, 0)
except ArithmeticError:
    print("Error: Arithmetic operation failed.")
except ZeroDivisionError:
    print("Error: Division by zero is not allowed.")
