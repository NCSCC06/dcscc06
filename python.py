# Get input from the user
try:
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
except ValueError:
    print("Invalid input. Please enter numerical values.")
    exit()

# Perform arithmetic operations
sum_result = num1 + num2
difference_result = num1 - num2
product_result = num1 * num2

# Handle division by zero
if num2 != 0:
    division_result = num1 / num2
else:
    division_result = "Cannot divide by zero"

# Display the results
print(f"Sum: {sum_result}")
print(f"Difference: {difference_result}")
print(f"Product: {product_result}")
print(f"Division: {division_result}")