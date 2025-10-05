def wisdom():
	print("You have to know when to hold em")

def wisdom():
	print("Life is like a box of chocolate...")

wisdom()


def fizz_buzz(x):
	if x % 3 == 0 and x % 5 == 0:
		print(f"{x} FIZZ BUZZ")
	elif x % 3 == 0:
		print(f"{x} FIZZ")
	elif x % 5 == 0:
		print(f"{x} BUZZ")
	else:
		print(x)


fizz_buzz(15)

# Returning True or False

def is_even(x):
	if x % 2 == 0:
		return True
	else:
		return False
print(is_even(99))

def is_even(x):
	if x % 2 == 0:
		return True
	else:
		return False
print(is_even(24))

# Assigning function output to a variable:

def is_even(x):
	if x % 2 == 0:
		return True
	else:
		return False
my_var = is_even(98)

print(my_var)

# Function can have more than one argument

def add(a,b):
	c = a + b
	return c

print(add(5,3))

def namer(first, last):
	print(f"Hello {first} {last}, nice to meet you!")

namer("Ade", "Omer")

# Using default arguments

def namer(first = "John", last = "Elder"):
	print(f"First name: {first}") 
	print(f"last name: {last}")

namer()

def namer(first = "John", last = "Elder"):
	print(f"First name: {first}") 
	print(f"last name: {last}")

namer("Ade", "Omer")

def namer(first = "John", last = "Elder"):
	print(f"First name: {first}") 
	print(f"last name: {last}")

namer("Ade")


# QUESTIONS
# Create a function that asks a persons name, allows them to enter 
# the name, and then prints out a welcome message with that name.


def persons_name(first_name, last_name):
	first_name = input("What is your first name? ")
	last_name = input("What is your last name? ")
	print(f" I am happy to welcome {first_name} {last_name} to my house!")

persons_name("a", "b")

# Write some code using the same fizz_buzz function but have it 
# print out all numbers between 1 and 100 by calling the function 
# 100 times.

def fizz_buzz(x):
	for x in range (1, 101):
		print(f"{x}")

fizz_buzz(1)

# Re-write the fizz_buzz function to prompt a user to enter a 
# number and then return the function result. 

def fizz_buzz():
	user_a = ("Enter a number: ")
