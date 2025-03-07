def divide_numbers(num1, num2):
    if num2 == 0:
        raise Exception("Cannot divide by zero! Please enter a valid divisor.")
    else:
        result = num1 / num2
        print(f"Result: {result}")

try:
    divide_numbers(10, 0)
except Exception as e:
    print(f"Error: {e}")
