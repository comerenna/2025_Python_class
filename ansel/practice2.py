Problem # 1: Discount Calculation Scenario:

# A store is offering different discounts based on the purchase amount.
# If the amount is greater than or equal to 5000, the customer gets a 20% discount.
# If the amount is between 2000 and 4999, the customer gets a 10% discount.
# If the amount is between 1000 and 1999, the customer gets a 5% discount.
# If the amount is less than 1000, no discount is given.

# Task: Write a program that takes the purchase amount 
# as input and prints the applicable discount percentage.

purchase_amount = int(input("Enter the purchase amount: "))

discount = 0

if purchase_amount >= 5000:
    discount = 0.2
    amount = purchase_amount * discount
    finalamount = purchase_amount - amount
    print("The final amount is: ", finalamount)
elif purchase_amount >= 2000 and purchase_amount <= 4999:
    discount = 0.1
    aamount = purchase_amount * discount
    finalamount = purchase_amount - amount
    print("The final amount is: ", finalamount)
elif purchase_amount >= 1000 and purchase_amount <= 1999:
    discount = 0.05
    amount = purchase_amount * discount
    finalamount = purchase_amount - amount
    print("The final amount is: ", finalamount)
else:
    if purchase_amount < 1000:
        print("No discount is provided")

# Problem 2: Traffic Light Signal Scenario:

# You are writing a program for a traffic control system.
# If the light is "Red," print "Stop."
# If the light is "Yellow," print "Get ready."
# If the light is "Green," print "Go."

# Task: Take a color input from the user and print the appropriate message.

traffic_light = input("Enter the color of traffic light: ")

if traffic_light == "Red":
    print("Stop")
elif traffic_light == "Yellow":
    print("Get Ready")
else:
    if traffic_light == "Green":
        print("Go")

# Problem 3: Eligibility for Loan Approval Scenario:

# A bank wants to automate loan eligibility checks.
# If a person’s credit score is above 750 and their annual 
# income is greater than 500,000, they are eligible for a loan.
# If their credit score is between 600 and 750 and income is 
# between 300,000 and 500,000, they need a guarantor.
# If their credit score is less than 600, they are not eligible for a loan.

# Task: Write a program that takes credit score and 
# annual income as input and prints the eligibility status.

credit_score = int(input("Enter the credit score: "))
annual_income = int(input("Enter the person's annual income: "))

if credit_score > 750:
    if annual_income > 500000:
        print("They can get a loan")
    else:
        print("They are not eligible for a loan")
elif credit_score >= 600 and credit_score <= 750:
    if annual_income >= 300000 and annual_income <= 500000:
        print("They will need a Guarantor")
    else:
        print("They are not eligible for a loan")
else:
    if credit_score < 600:
        print("They are not eligible for a loan")

# Problem 4: Movie Ticket Pricing Scenario:

# A cinema offers different ticket prices based on the customer's age.
# If the age is below 5, the ticket is free.
# If the age is between 5 and 12, the ticket price is $5.
# If the age is between 13 and 60, the ticket price is $10.
# If the age is above 60, the ticket price is $7.

# Task: Write a program that takes the age as input and prints the ticket price.

customer_age = int(input("Enter the customer age: "))

if customer_age < 5:
    print("Ticket is free")
elif customer_age >= 5 and customer_age <= 12:
    print("The ticket price is $5")
elif customer_age >= 13 and customer_age <= 60:
    print("The ticket price is $10")
else:
    if customer_age > 60:
        print("The ticket price is $7")

# Problem 5: Grade Calculator Scenario:

# A school wants to calculate the grades of students based on their scores.
# If the score is 90 or above, the grade is "A".
# If the score is between 80 and 89, the grade is "B".
# If the score is between 70 and 79, the grade is "C".
# If the score is between 60 and 69, the grade is "D".
# If the score is below 60, the grade is "F".

# Task: Write a program that takes the score as input and prints the grade.

students_score= float(input("Enter the student score: "))

if students_score >= 90:
    print("The grade is", "A")
elif students_score >= 80 and students_score <= 89:
    print("The grade is", "B")
elif students_score >= 70 and students_score <= 79:
    print("The grade is", "C")
elif students_score >= 60 and students_score <= 69:
    print("The grade is", "D")
else:
    if students_score < 60:
        print("The grade is", "F")


# Problem 6: Temperature Classification Scenario: 
# A weather station needs to classify temperature ranges.
# If the temperature is below 0°C, print "Freezing".
# If the temperature is between 0°C and 15°C, print "Cold".
# If the temperature is between 16°C and 30°C, print "Warm".
# If the temperature is above 30°C, print "Hot".

#Task: Write a program that takes the 
# temperature as input and prints the classification.

temperature_ranges = float(input("Enter the temperature ranges: "))

if temperature_ranges < 0:
    print("It is Freezing")
elif temperature_ranges >= 0 and temperature_ranges <= 15:
    print("It is Cold")
elif temperature_ranges >= 16 and temperature_ranges <= 30:
    print("It is Warm")
else:
    if temperature_ranges > 30:
        print("It is Hot")


# Problem 7: Nested if for Password Strength Check Scenario:

# A website requires users to create secure passwords.
# If the password length is less than 8 characters, print "Weak password".
# If the password length is 8 or more characters, check:
# If it contains at least one number, print "Strong password".
# Otherwise, print "Moderate password".

# Task: Write a program that checks the strength of a password input.

password = input("Enter your password: ")
has_number = True

if len(password) < 8:
	print("It is a weak password")
	if len(password) >= 8:
		print("Check")
		if password >= 8 and has_number:
			print("It is a Strong Password")
else:
	print("It is a Moderate Password")