input_age = input("Provide me age \n")
day = input("Provide me day of the week \n")
age = int(input_age)
day = day.upper()


discount = 2

price = 12 if age >= 18 else 8

if day == "MONDAY":
    price -= discount

print(f"Your ticket price is ${price}")
