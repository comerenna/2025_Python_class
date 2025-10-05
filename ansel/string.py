name = "kelvin"
print(name.upper())

print(len(name))

print(name.capitalize())

name = input("Enter your name: ")
print(f"Hi Dear {name.upper()}!")

name = input("Enter your name: ")
name = name.lower()
print(name)

name = input("Enter your name: ")
print(f"The name {name} has {len(name)} characters")

f_name = input("Enter your first name: ")
l_name = input("Enter your last name: ")
print(f"My full name is {f_name.title()} {l_name.title()} and I like biking") 

# String Substitution
my_string = "I like %s and %s " %("Python" , "Coding")
print(my_string)


# String Slicing
my_self = "this is a magnificient match"
print(my_self[0:4])

# String concatenation
second_string = "the value of the process " + "is enticing"
print(second_string)

# Substitution using template (dictionary)
print("%(lang)s is fun" % {"lang": "Python"})

# Substition using format function
print("Python is a {0}, {1}".format("simple","language"))