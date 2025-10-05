# While Loops

num = 0
while num < 10:
	print(num)
	num += 1


num = 0
while num < 10:
	num += 1
	if num == 5:
		break
	print(num)


num = 0
while num < 10:
	num += 1
	if num == 5:
		continue
	print(num)

count = 1

while count <= 5:
	print(f"Count is: {count}")
	count +=1


# For Loops

for num in range(6):
	print(num)

for num in range(2, 6):
	print(num)

for num in range(6):
	print("I am happy!!!")

# Iterating inside a list

names = ["John", "Tim", "Mary", "Beatrice", "Bluto"]
for name in names:
	print(name)


fruit = "tomatoes"
for x in fruit:
	print(x)

#Using Else with FOR

for x in range(3):
	print(x)
else:
	print("All Done!!!")

for x in range(3):
	print(x)
print("All Done!!!")

# PASS statement

for x in range(3):
	pass


# Print out every number between 1 and 100, 
# one number per line, but if the number is divisible by three, 
# print out "Fizz"; if the number is divisible by five, 
# print out "Buzz"; and if the number is divisible by both three AND five, 
# print out FIZZ BUZZ. 


for num in range(1,101):
	if num % 3 == 0 and num % 5 == 0:
		print(f"FIZZ BUZZ")

for num in range(1,101):
	if num % 3 == 0 and num % 5 == 0:
		print(f"{num} FIZZ BUZZ")


for num in range(1,101):
	if num % 3 == 0 and num % 5 == 0:
		print(f"{num} FIZZ BUZZ")
	elif num % 3 == 0:
		print(f"{num} FIZZ")
	elif num % 5 == 0:
		print(f"{num} BUZZ")
	else:
		print(num)


num = 1
while num < 100:
	num += 1
	if num % 3 == 0 and num % 5 == 0:
		print(f"{num} FIZZ BUZZ")
	elif num % 3 == 0:
		print(f"{num} FIZZ")
	elif num % 5 == 0:
		print(f"{num} BUZZ")
	else:
		print(num)

# Create a multi-dimensional List with 4 items, 
# and each item is itself a List containing a person's name, 
# their address, and phone number (make up the info). 
# Loop through the List and output just each person's phone number. 

names = [["John", "5 Peters street", +2348023881539],
["Tim", "5 Mark street",+2349023881539],
["Mary","5 Mark street", +2348023881534], ["Beatrice","5 John street", +2348023881539]]
print(names[0][2])
print(names[1][2])
print(names[2][2])
print(names[3][2])


names = [["John", "5 Peters street", +2348023881539],
["Tim", "5 Mark street",+234023881539],
["Mary","5 Mark street", +2348023881534], ["Beatrice","5 John street", +2348023881439]]

for phone_num in names:
	if phone_num == +2348023881539 and +2349023881539 and +2348023881534 and +2348023881439:
		print(phone_num)


# Loop through the List from exercise 2 and print out the full 
# information of even items in the List 
# (ie the 2nd and 4th List in your multidimensional List)

for name in names:
	print(name[0:3])
	print(name[3:3])


for i in range(1,4):
	for j in range(1,4):
		print(i, "*", j, "=", i * j)