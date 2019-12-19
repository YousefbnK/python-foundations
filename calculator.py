def add(first_number, second_number):
	return first_number + second_number 

def subtract(first_number, second_number):
	return first_number - second_number

def multiply(first_number, second_number):
	return first_number * second_number

def divide(first_number, second_number):
	return first_number / second_number

try:
	first_number = float(raw_input("Enter the first number  "))
	second_number = float(raw_input("Enter the second number  "))
except ValueError:
	print("Invalid input, please enter number   ")
else:
	operation = raw_input("Choose the operation (+, -, /, *):  ")

if operation == "+":
	print("The answer is", add(first_number, second_number))

elif operation == "-":
	print("The answer is", subtract(first_number, second_number))

elif operation == "/":
	print("The answer is", divide(first_number, second_number))

elif operation == "*":
	print("The answer is", multiply(first_number, second_number))

else:
	print("Invalid input, please select operation")

