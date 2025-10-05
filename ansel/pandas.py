empty_list = []
empty_tuple = ()
empty_dict = {}
empty_string = ""
Nothing = None

if empty_list == []:
	print("It is an empty list")

if empty_tuple:
	print("It is not an empty tuple")

if not empty_string:
	print("This is an empty string")

if not Nothing:
	print("Then it is a nothing")

count = 1

while count <= 5:
	print("Count is: ", count)
	count +=1


for i in range(5):
	pass

for i in range(1,4):
	for j in range(1,4):
		print(i, "*", j, "=", i * j)