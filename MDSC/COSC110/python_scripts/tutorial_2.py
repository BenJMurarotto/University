age = input("Enter your current age in years: ")
age = int(age)
if age >= 100:
    print("You've already turned 100!")
elif age <= 0:
        print("Try again after you are born!")
else:
    years_to_100 = 100 - age
    print("You will be 100 in", years_to_100, "years!")
