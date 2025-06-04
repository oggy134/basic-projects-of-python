#Weight convertor using python

Weight=float(input("Enter your Weight: "))
unit=input(("Press k if it is in Kilograms or Press L if it is in pounds:\n"))

if unit=="K":
    Weight=Weight*2.205
    print(f"your Weight is {round(Weight,1)} in Pounds")
elif unit=="L":
    Weight=Weight/2.205
    print(f"your Weight is {round(Weight,1)} in Kilogram")
else:
    print(f"{unit} is invalid unit Try again")