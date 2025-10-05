# Question 1: A store sells apples at $5 each and bananas at $3 each. 
# Declare variables apples_price and bananas_price with appropriate values. 
# Calculate the total cost for purchasing 10 apples 
# and 7 bananas and store the result in total_cost

apples_price = int(input("Enter the apple price: "))
bananas_price = int(input("Enter the banana price: "))
total_cost = 10 * apples_price + 7 * bananas_price
print(f"The total cost: {total_cost}")

# Question 2: You have a monthly salary of $4,000 and expenses that 
# include rent ($1,200), groceries ($300), and miscellaneous ($500). 
# Calculate the amount left after expenses 
# and store it in a variable named remaining_balance.


monthly_salary = int(input("Enter the monthly salary: "))
rent = int(input("Enter the rent: "))
groceries = int(input("Enter the groceries: "))
miscelleneous = int(input("Enter the miscelleneous: "))
expenses = rent + groceries + miscelleneous
remaining_balance = monthly_salary - expenses
print(f"The remaining balance is: {remaining_balance}")

# Question 3: A team won 28 matches this season, 
# and last season they won 18 matches. 
# Declare variables current_season_wins 
# and last_season_wins with respective values. 
# Calculate the increase in matches won and store it in win_difference.

current_season_wins = int(input("Enter the current season wins: "))
last_season_wins = int(input("Enter the last season wins: "))

win_difference = current_season_wins + last_season_wins
print(f"The matches won: {win_difference}")


# Question 4: A travel company charges $250 per person for a 
# weekend trip and gives a $100 group discount for every 
# 5 people. If a group has 15 people Calculate the 
# total cost for the group and store it in group_trip_cost.

charge_per_person = int(input("Enter the charge per person: "))
discount_person = int(input("Enter the discount for each person: "))
number_of_person = int(input("Enter the number of person: "))
group_discount = number_of_person * discount_person
group_trip_cost = charge_per_person + group_discount
print(f"The total cost for the group: {group_trip_cost}")

# Question 5: An item costs $120, and 
# there is a discount of 15%. Calculate the final price 
# after the discount and store it in discounted_price.

item_cost = int(input("Enter the cost of item: "))
discount = int(input("Enter the discount of the item: "))
discounted_price = item_cost * discount/100
final_price = item_cost - discounted_price
print(f"The final price of the item: {final_price}")

# Question 6: A company produces 500 units daily and 
# sells each unit for $20. Declare variables units_per_day 
# and price_per_unit. Calculate the monthly revenue 
# assuming a 30-day month and store it in monthly_revenue

unit_per_day = int(input("Enter the unit produce per day: "))
price_per_unit = int(input("Enter the unit of sales per day: "))
total_sales_per_day = unit_per_day * price_per_unit	
monthly_revenue = 30 * total_sales_per_day
print(f"The monthly revenue in a month: {monthly_revenue}")

# Question 7: A farmer grows wheat on a 150-acre farm and 
# yields 3,000 kg per acre. Declare variables acreage and 
# yield_per_acre. Calculate the total wheat production 
# and store it in total_production.

yield_per_acre = int(input("Enter the yield per acre: "))
acreage = int(input("Enter the acre age farm: "))
total_production = yield_per_acre * acreage
print(f"The total wheat production: {total_production}")

# Question 8: A bakery makes $2 profit on each loaf of bread 
# sold. If they sell 200 loaves in a day, declare variables 
# profit_per_loaf and loaves_sold. Calculate the daily profit 
# and store it in daily_profit.

profit_per_loaf = int(input("Enter the profit made on each loaf: "))
loaves_sold = int(input("Enter the amount of loaves sold: "))
daily_profit = profit_per_loaf * loaves_sold
print(f"The daily profit made in loaves sold in a day: {daily_profit}")


# Question 9: You are planning an event for 120 attendees. 
# The venue rental is $800, and catering costs $25 per person. 
# Declare variables venue_cost, catering_cost_per_person, 
# and number_of_attendees. Calculate the total cost of 
# the event and store it in event_total_cost.

venue_cost = int(input("Enter the venue rental cost: "))
catering_cost_per_person = int(input("Enter the catering cost per person: "))
number_of_attendees = int(input("Enter the number of attendees: "))
event_per_attendees = catering_cost_per_person * number_of_attendees
event_total_cost = venue_cost + event_per_attendees
print(f"The toatl cost for the event: {event_total_cost}")

# Question 10: A school's annual fee per student is $1,500, 
# and they provide a 5% sibling discount. Declare variables
# annual_fee and sibling_discount_percent. 
# Calculate the discounted fee for one sibling and 
# store it in sibling_discounted_fee.

annual_fee = int(input("Enter the annual fee per student: "))
sibling_discount_percent = int(input("Enter the sibling discount: "))
discounted_fee = annual_fee * sibling_discount_percent/100
sibling_discounted_fee = annual_fee - discounted_fee
print(f"The discounted fee for one sibling: {sibling_discounted_fee}")
