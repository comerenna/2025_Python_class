my_list = []
another_list = list()

my_tuple = (23, 45, 2, 56, 12, 100)
my_list = list(my_tuple)
print(my_list)


names = ["John", "Tim", "Mary", "Beatrice", "Bluto"]
print(names[1:3])
print(names[2])
print(names[:1])
print(names[:4])
print(names)

variable_1 = "Tim"
names = ["John", variable_1, "Mary", 41, "Bluto"]
print(names[1])

names = ["John", "April"]
print(len(names))

# adding names to a list, you use the append()

names = ["John", "April"]
names.append("Bob")
print(names)

# adding integer or string in a list, you use insert() 
# insert takes two argument position(index, "paul")


names = ["John", "Tim"]
names.insert(1,"Bob")
print(names)

# To add multiple items to the end of your list, use extend().

names = ["John", "Tim"]
names.extend(["Peter", "Eze"])
print(names)

# Removing an item from a list, we can use the remove()

names = ["John", "Tim", "Mary", "Beatrice", "Bluto"]
names.remove("Bluto")
print(names)

# Removing in a specific index

names = ["John", "Tim", "Mary", "Beatrice", "Bluto"]
names.pop(1)
print(names)

# Multi-Dimensional List

names = ["John", "Tim", "Mary", "Beatrice", "Bluto", [1,2,3,4]]
print(names[5][2])

numbers = [1,2,3,4]
names = ["John", "Tim", "Mary", "Beatrice", "Bluto", numbers]
print(names[5][1])

# Create a List with the names of five people you know and output 
# the second name to the screen. 
names = ["John", "Tim", "Mary", "Beatrice", "Bluto"]
print(names[1])

# Create a List where the first item in the List is a math problem, 
# like 1 + 1 and the rest of the items are names. 
# Output the first item to the screen
a = 5
b = 10
c = a + b
names = [c,"John", "Tim", "Mary", "Beatrice", "Bluto"]
print(names[0])

# Create a multi-dimensional List with 4 items, 
# and each item is itself a List containing 
# a person's name, their address, and phone number (make up the info). 
# Output the second item in your multidimensional List.

names = [["John", "5 Peters street", "08023881539"],
["Tim", "5 Mark street","09023881539"],
["Mary","5 Mark street", "08023881534"], ["Beatrice","5 John street", "08023881539"]]
print(names[1][2])

# Output just the phone number of the third item in your 
# List from the last question.

print(names[2][2])