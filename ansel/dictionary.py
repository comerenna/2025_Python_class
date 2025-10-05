my_dict = {}
another_dict = dict()


favorite_pizza = {"John": "Pepperoni", "Tim": "Mushroom", "Mary": "Cheese", "Beatrice": "Ham and Onion", "Bluto": "Supreme"}
print(favorite_pizza["John"])
print(favorite_pizza["Beatrice"])

print("Tim" in favorite_pizza)

# Adding and removing items from dictionary

favorite_pizza = {"John": "Pepperoni", "Tim": "Mushroom", "Mary": "Cheese", "Beatrice": "Ham and Onion", "Bluto": "Supreme"}
favorite_pizza["Bob"] = "Tuna"
print(favorite_pizza)


favorite_pizza = {"John": "Pepperoni", "Tim": "Mushroom", "Mary": "Cheese", "Beatrice": "Ham and Onion", "Bluto": "Supreme"}
favorite_pizza.pop("Mary")
print(favorite_pizza)

# Dictionary Odds and End

user_name = "John"
favorite_pizza = {user_name: "Pepperoni", "Tim": "Mushroom", "Mary": "Cheese", "Beatrice": "Ham and Onion", "Bluto": 41}
print(favorite_pizza)
print()
print(favorite_pizza[user_name])
print()
print(favorite_pizza["Bluto"] + 10)

# Alternative way to write a dictionary
favorite_pizza = {
"John": "Pepperoni", 
"Tim": "Mushroom", 
"Mary": "Cheese", 
"Beatrice": "Ham and Onion", 
"Bluto": " Supreme"
}

# Finding the keys and values of a dictionary

favorite_pizza = {
"John": "Pepperoni", 
"Tim": "Mushroom", 
"Mary": "Cheese", 
"Beatrice": "Ham and Onion", 
"Bluto": " Supreme"
}
print(favorite_pizza.keys())
print()
print(favorite_pizza.values())

# Looping dictionary to get keys and values

favorite_pizza = {
"John": "Pepperoni", 
"Tim": "Mushroom", 
"Mary": "Cheese", 
"Beatrice": "Ham and Onion", 
"Bluto": " Supreme"
}

for x, y in favorite_pizza.items():
	print(f"key:{x} values: {y}")

	
# When to use dictionary versus when to use list

favorite_pizza = {
1: "Pepperoni", 
2: "Mushroom", 
3: "Cheese", 
4: "Ham and Onion", 
5: " Supreme"
}

print(favorite_pizza[5])

# Create your own Dictionary, with five of your friends' names and 
# their phone numbers.

diary = { "Jamiu": +23470653526,
"Mojeed": +23426881539, 
"Abio": +2347016214557,
"Omer": +23450267845,
"Eki": +23456994875	
}
print(diary)

#Create a program using your answer to exercise 1 that prompts a 
#user to enter a name from your list your five friends, and then 
#returns the phone number for that specific friend.

diary = { "Jamiu": +23470653526,
"Mojeed": +23426881539, 
"Abio": +2347016214557,
"Omer": +23450267845,
"Eki": +23456994875	
}
print(diary["Mojeed"])

# Add a feature to your code from exercise 2 that allows people to 
# add or delete a name from the Dictionary, then return the 
# updated Dictionary to the screen. 


# To add to the list

diary["Gbenga"] = +23456994857

print(diary)

# To remove from the list
diary.pop("Eki")
print(diary)


#Create a loop that cycles through your Dictionary from exercise 1 
#and outputs (one per line) "My friend X's phone number is: xxx-xxx-xxxx" 
#replacing the x's with the persons actual name and phone number.

for x,y in diary.items():
	print(f"My friend {x} phone number is: {y}")