import math


amount = int(input("Please Enter Amount for square root: "))

square_root = math.sqrt(amount)

# Calculate the number of notes of 100, 50, and 10
notes_100 = amount // 100
amount %= 100
notes_50 = amount // 50
amount %= 50
notes_10 = amount // 10

# Print the results
print("Notes of 100 squares:", notes_100)
print("Notes of 50 squares:", notes_50)
print("Notes of 10 squares:", notes_10)