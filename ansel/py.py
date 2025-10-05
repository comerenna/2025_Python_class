# A website requires users to create secure passwords.
# If the password length is less than 8 characters, print "Weak password".
# If the password length is 8 or more characters, check:
# If it contains at least one number, print "Strong password".
# Otherwise, print "Moderate password".


weight = int(input("Enter the weight: "))
unit = input("Enter the unit of the weight: ")


if unit.upper() == "L":
    converter = weight * 0.5
    print(f"You have {converter} kilo")
else:
    converter = weight / 0.5
    print(f"You have {converter} pounds")