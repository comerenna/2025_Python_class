# Q1: Movie Ticket Pricing
# Scenario: A cinema has different ticket prices based on age.
# Task: Write a program that asks for the customer's age
# and prints the ticket price.

# Child (0-12): ₹100
# Teen (13-17): ₹150
# Adult (18-59): ₹200
# Senior (60+): ₹120

customers_age = int(input("Enter the customers age: "))
child = 100
Teen = 150
Adult = 200
Senior_Adult = 120

if customers_age <= 12:
	print("The ticket price: ", child )
elif customers_age >= 13 and customers_age <= 17:
	print("The ticket price: ", Teen)
elif customers_age >= 18 and customers_age <=59:
	print("The ticket price: ", Adult)
else:
	print("The ticket price: ", Senior_Adult)


# Q2: Simple Weather Advisory
# Scenario: A local weather station provides basic weather advisories.
# Task: Create a program that takes the current temperature (in Celsius)
# and provides an appropriate advisory.

# Below 0: "It's freezing! Wear warm layers."
# 0-10: "It's very cold. Wear a heavy jacket."
# 11-20: "It's cool. A light jacket would be good."
# 21-30: "It's pleasant. Enjoy the weather!"
# Above 30: "It's hot. Stay hydrated!

current_temperature = int(input("Enter the current temperature: "))

if current_temperature < 0:
	print("It's freezing! Wear warm layers.")
elif current_temperature >=0 and current_temperature <=10:
	print("It's very cold. Wear a heavy jacket.")
elif current_temperature >= 11 and current_temperature <= 20:
	print("It's cool. A light jacket would be good.")
elif current_temperature >= 21 and current_temperature <= 30:
	print("It's pleasant. Enjoy the weather!")
else:
	print("It's hot. Stay hydrated!")


# Q3:Restaurant Tip Calculator
# Scenario: A restaurant suggests tips based on service quality.
# Task: Write a program that asks for the bill amount 
# and service quality (Excellent, Good, Fair, Poor) 
# and calculates the suggested tip.

# Excellent: 20% tip
# Good: 15% tip
# Fair: 10% tip
# Poor: 5% tip

# bill_amount = int(input("Enter the bill amount: "))
tips = int(input("Enter the tips based on service quality received: "))

if tips >= 20:
    print("The service quality is Excellent")
elif tips >= 15 and tips < 20:
    print("The service quality is Good")
elif tips >= 10 and tips < 15:
    print("The service quality is Fair")
else:
    print("The service Poor")


# Q5: Blood Donation Eligibility
# Scenario: A blood donation camp screens donors based on basic criteria.
# Task: Write a program that determines if a person is eligible to donate blood based on:

# Age (must be 18-65)
# Weight (must be above 50 kg)
# Last donation (must be more than 3 months ago)


age = int(input("Enter the age: "))
weight = int(input("Enter the weight: "))

if age >= 18 and age <= 65:
    if weight > 50:
        print("He is eligible to donate blood")
    else:
        print("He donated last three month")
else:
    print("He is not eligible to donate blood")



# Q6: Simple Car Insurance Premium Estimator
# Scenario: A car insurance company determines premiums 
# based on driver's age and car type.
# Task: Create a program that estimates the premium:

# Age below 25: High risk
# Age 25-40: Medium risk
# Age above 40: Low risk
# Car types: Economy, Sedan, Luxury (increasing premiums in that order)

drivers_age = int(input("Enter the drivers age: "))
car_type = int(input("Enter the car type: "))

drivers_age = int(input("Enter the drivers age: "))
car_type = input("Enter the car type: ")

if drivers_age < 25 and car_type == "Economy":
    print("The risk is High")
elif drivers_age >= 25 and drivers_age <= 40:
    if car_type == "Sedan":
        print("The risk is Medium")
else:
    if drivers_age > 40 and car_type == "Luxury":
        print("The risk is Low")


# Q7:
# College Admission Predictor
# Scenario: A college has different admission criteria based on exam scores.
# Task: Write a program that predicts admission chances based on exam score:

# Below 60: "Admission unlikely"
# 60-79: "Admission possible"
# 80-89: "Admission probable"
# 90 and above: "Admission assured"

exam_scores = int(input("Enter the exam score: "))

if exam_scores < 60:
    print("Admission unlikely")
elif exam_scores >= 60 and exam_scores <= 79:
    print("Admission possible")
elif exam_scores >= 80 and exam_scores <= 89:
    print("Admission probable")
else:
    if exam_scores >= 90:
        print("Admission Assured")

# Q8:
# Simple Loan Approval System
# Scenario: A bank has basic criteria for loan approval.
# Task: Create a program that determines loan approval based on:

# Credit Score (Good/Fair/Poor)
# Annual Income (Above/Below ₹500,000)
# Employment Status (Employed/Self-employed/Unemployed)





# Q9:
# Mobile Plan Recommender
# Scenario: A telecom company recommends plans based on usage.
# Task: Write a program that suggests a plan based on monthly data usage:

# 0-2 GB: "Basic Plan"
# 2-5 GB: "Standard Plan"
# 5-10 GB: "Heavy User Plan"
# Above 10 GB: "Unlimited Plan"

ddata_usage = int(input("Enter the data usage: "))

if data_usage >= 0 and data_usage <= 2:
    print("Basic Plan")
elif data_usage > 2 and data_usage <= 5:
    print("Standard Plan")
elif data_usage > 5 and data_usage <= 10:
    print("Heavy User Plan")
else:
    print("Unlimited Plan")

# Q10:
# Simple Health Risk Assessment
# Scenario: A health app provides basic risk assessment based on BMI.
# Task: Create a program that calculates BMI (weight in kg / (height in m)^2) 
# and provides a health risk assessment:

# Below 18.5: "Underweight"
# 18.5-24.9: "Normal weight"
# 25-29.9: "Overweight"
# 30 and above: "Obese"

weight = float(input("Enter the weight: "))
height = float(input("Enter the height: "))

BMI = weight / (height * height)

if BMI < 18.5:
    print("You are Underweight")
elif BMI >= 18.5 and BMI <= 24.9:
    print("You are having Normal weight")
elif BMI >= 25 and BMI <= 29.9:
    print("You are Overweight")
else:
    if BMI > 30:
        print("You are Obese")

