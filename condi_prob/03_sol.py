input_score = input("Provide me score \n")
score = int(input_score)
if score >= 101:
    print("Please verify your grade again")
    exit()

grade = "A" if score >= 90 else "B" if score >= 80 else "C" if score >= 70 else "D" if score >= 60 else "F"

print(f"Your grade is {grade}")

# if score >= 90:
#     grade = "A"
# elif score >= 80:
#     grade = "B"
# elif score >= 70:
#     grade = "C"
# elif score >= 60:
#     grade = "D"
# else:
#     grade = "F"
# print(f"Your grade is {grade}")