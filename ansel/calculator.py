num1 = float(input("Enter your first number: "))
num2 = float(input("Enter your second number: "))
operator = input("Enter an operator(*, +, -, /, **): ")

if operator == "*":
	print(f"Result: {num1 * num2}")
elif operator == "+":
	print(f"Result: {num1 + num2}")
elif operator == "-":
	print(f"Result: {num1 - num2}")
elif operator == "**":
	print(f"Result: {num1 ** num2}")
elif operator == "/":
	if num2 != 0:
		print(f"Result: {num1 / num2}")
	else:
		print(f"Error: Can't be divided by zero")
else:
	print(f"It is an invalid operator.")