# Prompt the user to enter their weekly pocket money and convert it to a float for calculations
pocketMoney = float(input("How much pocket money do you get per week?: "))

# Prompt the user to enter how much of their pocket money they spend each week
spentMoney = float(input("How much of your pocket money do you spend per week?: "))

# Calculate the leftover money after spending
leftover = pocketMoney - spentMoney

# Calculate annual savings based on the leftover money (52 weeks in a year)
savings = leftover * 52

# Display the total savings for the year
print("You will save", savings, "this year")
