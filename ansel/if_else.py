age = int(input("Enter your age: "))
has_ID = True

if age >= 18 and has_ID:
	print("You can vote")
else:
	print("You can't vote")

# Nested Conditional

age = 25
has_ticket = True

if age >= 18:
	if has_ticket:
		print("Welcome to the concert.")

	else:
		print("You need a ticket")
else:
	print("You are too young.")

# Imagine you are building a weather.com portal. Now on this portal
# you have been asked to add functionality as follows: For any
# temperature user entered, you need to say whether it is High/Low
# Any temperature above 40C considered to be high
# Any temperature lower than 10C considered to be low

temp = int(input("Enter the temperature: "))

if temp > 40:
	print("It is too HIGH")
elif temp >= 11 and temp <= 39:
	print("It is Moderate")
elif temp < 10:
	print("It is too LOW")
else:
	print("It is inconsiderate")

# Imagine you are going to movie with family. You, spouse
# and your kid who is 9 years old. Tuesday offer in PVR,
# for adults who is above 18 years ticket price is 100 Rupees.
# For kids who are below 18 years ticket price is 50 Rupees.
# How much to pay?

husband = int(input("Enter the adult age: "))
wife = int(input("Enter the adult age: "))
kids = int(input("Enter the kids age: "))

amount = 0

if husband > 18:
	amount += 100
if wife > 18:
	amount += 100
if kids < 18:
	amount += 50
else:
	amount += 100
	
print(f"The amount to pay: {amount}")

# If you are a developer at Zomaoto. They are launching a new offer
# If you order above 500 Rupees, you will get 20% off.
# If you order below 500 Rupees, you will get 10% off.
# Also there is another special offer, if you order above 500 and 
# your shipping distance is below 10 KM then you get additional 5%
# off. If it is above 10 KM then 2% additional off.

# Tell me how much I have to pay if I offered for 1000 Rupees
# and my shipping distance is 5KM


amount = int(input("Enter the order_amount: "))
distance = int(input("Enter the distance: ")) 

discount = 0

if amount > 500:
	discount = 0.2
	if distance < 10:
		discount = discount + 0.05
	else:
		discount = discount + 0.02

else:
	discount = 0.1

discountAmount = amount * discount
finalprice = amount - discountAmount

print(f"The amount to pay: {finalprice}")


# If you are a developer at Zomaoto. They are launching a new offer
# If you order above 500 Rupees, you will get 20% off.
# If you order below 500 Rupees, you will get 10% off.
# Also there is another special offer, if you order above 500 and 
# your shipping distance is below 10 KM then you get additional 5%
# off. If it is above 10 KM then 2% additional off.

# Above offer is for normal user but if you within the 10KM radius
# and you are senior citizen (above 60 years old) then special
# offer of 5% extra

# Tell me how much I have to pay if I offered for 1000 Rupees
# and my shipping distance is 5KM and my age is 65 years


amount = int(input("Enter the order_amount: "))
distance = int(input("Enter the distance: ")) 
age = int(input("Enter your age: "))

discount = 0

if amount > 500:
	discount = 0.20
	if distance <= 10:
		discount = discount + 0.05
		if age > 60:
			discount = discount + 0.05
	else:
		discount = discount + 0.02
else:
	discount = 0.1

discountAmount = amount * discount

finalprice = amount - discountAmount

print(f"The amount to pay: {finalprice}")

# If you are a developer at Zomaoto. They are launching a new offer
# If you order above 500 Rupees, you will get 20% off.
# If you order below 500 Rupees, you will get 10% off.
# Also there is another special offer, if you order above 500 and 
# your shipping distance is below 10 KM then you get additional 5%
# off. If it is above 10 KM then 2% additional off.

# Above offer is for normal user but if you within the 10KM radius
# and you are senior citizen (above 60 years old) then special
# offer of 5% extra

# If order is below 500 and if you are below 25 years, 
# then we give you 5% extra off

# Tell me how much I have to pay if I offered for 1000 Rupees
# and my shipping distance is 5KM and my age is 65 years

amount = int(input("Enter the order_amount: "))
distance = int(input("Enter the distance: ")) 
age = int(input("Enter your age: "))

discount = 0

if amount > 500:
	discount = 0.20
	if distance <= 10:
		discount = discount + 0.05
		if age > 60:
			discount = discount + 0.05
	else:
		discount = discount + 0.02
else:
	discount = 0.1
	if age < 25:
		discount = discount + 0.05

discountAmount = amount * discount

finalprice = amount - discountAmount

print(f"The amount to pay: {finalprice}")


# Imagine that you are working for TCS and its the appraisal time
# For the appraisal they follow the below rule.
# for rating 4.5+ then 10% hike
# for rating between 3+ to 4.5 then 7% hike
# for rating between 2 to 3 then 3% hike
# Anything below 2, no hikes


# Solution 1
amount = int(input("Enter the CTC amount: "))
rating = float(input("Enter the rating value: "))

hikePercent = 0

if rating >= 4.5:
	hikePercent = 0.1
if rating >= 3:
	if rating < 4.5:
		hikePercent = 0.07
if rating >=2:
	if rating < 3:
		hikePercent = 0.03
if rating < 2:
	hikePercent = 0

hike_cal = amount * hikePercent
print(f"The final amount is: {hike_cal}")

# Solution 2
amount = int(input("Enter the CTC amount: "))
rating = float(input("Enter the rating value: "))

hikePercent = 0

if rating >= 4.5:
	hikePercent = 0.1
if rating > 3 and rating < 4.5:
	hikePercent = 0.07
if rating > 2 and rating < 3:
	hikePercent = 0.03
if rating < 2:
	hikePercent = 0

hike_cal = amount * hikePercent
print(f"The final amount is: {hike_cal}")


# Solution 3

amount = int(input("Enter the CTC amount: "))
rating = float(input("Enter the rating value: "))

hikePercent = 0

if rating >= 4.5:
	hikePercent = 0.1
elif rating > 3 and rating < 4.5:
	hikePercent = 0.07
elif rating > 2 and rating < 3:
	hikePercent = 0.03
else:
	hikePercent = 0

hike_cal = amount * hikePercent
print(f"The final amount is: {hike_cal}")



# Imagine that you are building a credit risk application, 
# you need to check the outstanding amount (loan taken - paid)
# and check: 
# if the outstanding amount is above 500000 then is High risk account
# if the outstanding amount is  below or equal to 500000 the moderate risk

loan_taken = int(input("Enter the loan taken: "))
amountPaid = int(input("Enter the amount paid: "))
outstanding_amount = loan_taken - amountPaid

if outstanding_amount > 500000:
	print("High Risk Account")
else:
	print("Moderate Risk Account")

# Imagine you are a grocery operator. Whenever you are doing the billing, 
# you have to calculate the total amount base on the items purchased.
# and for all the total amount above 500, you give 10% discount
# and any amount below that, you give 5% off.
# Finally, tell to customer how much to pay if 
# item1 = 100, item2 = 300 and item3 = 400

item1_purchased = int(input("Enter the items price: "))
item2_purchased = int(input("Enter the items price: "))
item3_purchased = int(input("Enter the items price: "))
total_amount = item1_purchased + item2_purchased + item3_purchased

#discount = 0

if total_amount > 500:
	discount = 0.1 
else:
	discount = 0.05

amountDisc = discount * total_amount

final_amount = total_amount - amountDisc
print(f"The total_amount is: {final_amount}")


# Write a program that utilizes the concept of conditional execution, 
# takes a string as input, and:
# prints the sentence "Yes - Spathiphyllum is the best plant ever!" 
# to the screen if the inputted string is "Spathiphyllum" (upper-case)
# prints "No, I want a big Spathiphyllum!" 
# if the inputted string is "spathiphyllum" (lower-case)
prints "Spathiphyllum! Not [input]!" otherwise. 
#Note: [input] is the string taken as input.

plant_name = input("Enter the name of plant: ")
if plant_name == "Spathiphyllum":
    print("Yes -", plant_name.title(), "is the best plant ever!")
elif plant_name != "spathiphyllum":
    print("Spathiphyllum!", "Not", plant_name,"!")
else:
    print("No,", "I want a big", plant_name.title())


#("-----------TAX CALCULATOR________________")

# if the citizen's income was not higher than 85,528 thalers, 
# the tax was equal to 18% of 
# the income minus 556 thalers and 2 cents (this was the so-called tax relief)
# if the income was higher than this amount, 
# the tax was equal to 14,839 thalers and 2 cents, 
# plus 32% of the surplus over 85,528 thalers.

income = float(input("Enter the annual income: "))

if income < 85528:
    tax = 0.18 * income - 556.2
else:
    if income > 85528:
        tax = 14839.2 + 0.32 * (income - 85528)
tax = round(tax, 0)
print("The tax is:", tax, "thalers")


is_hot = False
is_cold = True

if is_hot:
	print("It is a hot day")
	print("Drink plenty of water")
elif is_cold:
	print("It is a cold day")
	print("Wear warm clothes")
else:
	print("It is a lovely day")
	print("Enjoy your day")

# A price of house is 1000000 rupees and
# if the buyer has a good credit score,
# they need to put down 10%, otherwise
# they need to put down 20%.
# calculate the downpayment

house_price = int(input("the price of house: "))
credit_score = True
discout = 0

if credit_score == True:
    down_payment = 0.1 * house_price
    print(f"The down payment will be {down_payment}")
else:
    down_payment = 0.2 * house_price
    print(f"The down payment will be {down_payment}")

# if temperature is greater than 30, it is a hot day
# otherwise, if temperature is less than 10, 
# it is a cold day, otherwise it is neither a hot day

temp = int(input("Enter the temperature for each day: "))

if temp > 30:
    print("It is a hot day")
elif temp < 10:
    print("It is a cold day")
else:
    print("It is neither hot or cold")

# If a name is less than three(3) characters long, name must 
# be at least three characters. Otherwise, if the name is 
# more that fifty(50) characters, name an be a maximum of 
# fifty (50) characters, names look good

names = str(input("Enter the names you know of: "))

if len(names) < 3:
    print(f" the {names} must be at least three character")
elif len(names) > 10:
    print(f"The {names} can be a maximum of fifty characters")
else:
    print(f"The {names} looks good.")


# If an applicant has high income and good credit score
# he or she should be eligible for a loan

# Solution 1
high_income = False
good_credit_score = True

if high_income and good_credit_score:
    print("He is eligble for a loan")
else:
    print("The loan will be denied")

# Solution 2
high_income = False
good_credit_score = True

if high_income or good_credit_score:
    print("He is eligble for a loan")
else:
    print("The loan will be denied")

# Solution 3
has_criminal_record = True
good_credit_score = True

if has_criminal_record or good_credit_score:
    print("He is eligble for a loan")
else:
    print("The loan will be denied")

# Solution 4
has_criminal_record = False
good_credit_score = True

if good_credit_score and not has_criminal_record:
    print("He is eligble for a loan")
else:
    print("The loan will be denied")

has_criminal_record = False
good_credit_score = True

if good_credit_score and has_criminal_record:
    print("He is eligble for a loan")
else:
    print("The loan will be denied")