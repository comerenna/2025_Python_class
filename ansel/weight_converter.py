weight = int(input("Enter the weight: "))
unit = input("Enter the unit of the weight: ")


if unit.upper() == "L":
    converter = weight * 0.5
    print(f"You have {converter} kilo")
else:
    converter = weight / 0.5
    print(f"You have {converter} pounds"