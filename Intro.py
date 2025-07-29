## Intro to Python: Basic Arithmetic Operations
# This script performs basic arithmetic operations (addition, subtraction, multiplication, and division)
# based on user input. It demonstrates input handling, conditionals, arithmetic, and simple error checking.

# Ask the user to enter the first number and convert it to a float
numb1 = float(input("Enter first number: "))

# Ask the user to enter the second number and convert it to a float
numb2 = float(input("Enter second number: "))

# Ask the user which operation they want to perform
operation = input("Enter operation (+, -, *, /): ")

# Check which operation the user selected and perform the calculation accordingly
if operation == "+":
    result = numb1 + numb2  # Addition
    print(f"The result of {numb1} + {numb2} is: {result}")

elif operation == "-":
    result = numb1 - numb2  # Subtraction
    print(f"The result of {numb1} - {numb2} is: {result}")

elif operation == "*":
    result = numb1 * numb2  # Multiplication
    print(f"The result of {numb1} * {numb2} is: {result}")

elif operation == "/":

    # Check to avoid division by zero
    if numb2 != 0:
        result = numb1 / numb2  # Division
        print(f"The result of {numb1} / {numb2} is: {result}")
    else:
        print("Error: Cannot divide by zero. Please enter a non-zero second number.")

else:
    # Handle invalid operation input
    print("Invalid operation entered. Please enter one of +, -, *, /.")
