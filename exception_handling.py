# Try-Except block

try:
    age = int(input("25"))
    print(f"Your age is {age}")
except ValueError:
    print("Please enter a valid number.")

# Try-Except-Finally

try:
    result = 10 / 0
except ZeroDivisionError:
    print("Division by zero!")
finally:
    print("End of try-except block.")
