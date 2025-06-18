age = input("Privide me age \n")
int_age = int(age)

if int_age < 13:
    print("You are a child")
elif int_age < 20:
    print("You are a teenager")
elif int_age < 59:
    print("You are an adult")
else:
    print("You are senior")