roll_numbers = [1, 2, 3, 5, 6, 8, 10]

print("Roll Numbers:", roll_numbers)

for i in range(1, max(roll_numbers) + 1):
    if i not in roll_numbers:
        print("Missing Roll No:", i)