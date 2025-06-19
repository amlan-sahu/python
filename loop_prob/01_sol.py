numbers = [1, -2, 3, -4, 5, 6, -7, -8, 9, 10]
positive_number_count = 0
for number in numbers:
    # print(number)
    if number > 0:
        positive_number_count += 1

print(f"Positive numbers count: {positive_number_count}")